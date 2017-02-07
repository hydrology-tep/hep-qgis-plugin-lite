"""
***************************************************************************
   WorkflowGetDialog.py
***************************************************************************
"""

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox
import codecs
from processing.core.Processing import Processing
from processing.core.parameters import ParameterString
from processing.core.parameters import ParameterBoolean
from processing.core.parameters import ParameterSelection
from processing.core.parameters import ParameterNumber
from processing.gui.AlgorithmDialogBase import AlgorithmDialogBase
from processing_workflow.Workflow import Workflow
from processing_workflow.StepDialog import StepDialog, NORMAL_MODE, BATCH_MODE
from processing_workflow.WorkflowUtils import WorkflowUtils
from processing.gui.AlgorithmDialog import AlgorithmDialog
from processing_workflow.WrongWorkflowException import WrongWorkflowException
import os, shutil
from os.path import expanduser
import fnmatch, re, subprocess, glob

# Dialog for sharing workflows
class WorkflowGetDialog(AlgorithmDialogBase):
    def __init__(self, workflowAction):
		QtGui.QDialog.__init__(self)
		self.workflowProvider = workflowAction.workflowProvider
		self.setupUi()
		self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinMaxButtonsHint)
        
        	# set as window modal
		self.setWindowModality(1)

		self.workflow = Workflow()

		self.help = None
		self.update = True #indicates whether to update or not the toolbox after closing this dialog
		self.executed = False

    def setupUi(self):

		self.setFixedSize(318,318)
		self.setWindowTitle("Get WOIS Workflow")
		self.setWindowIcon(WorkflowUtils.workflowIcon())
		self.tabWidget = QtGui.QTabWidget()
		self.tabWidget.setMaximumSize(QtCore.QSize(350, 10000))
		self.tabWidget.setMinimumWidth(300)

		self.home_path = expanduser("~")
		self.workflows_path = self.home_path + "/.qgis2/python/plugins/processing_workflow/workflows"
        
		#left hand side part
       		#==================================
		self.verticalLayout = QtGui.QVBoxLayout()
		self.verticalLayout.setSpacing(2)
		self.verticalLayout.setMargin(0)
		
		self.horizontalLayout = QtGui.QHBoxLayout()
		self.horizontalLayout.setSpacing(2)
		self.horizontalLayout.setMargin(0)
		self.horizontalLayout.addWidget(self.tabWidget)
		
		self.buttonBox = QtGui.QDialogButtonBox()
	        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)

		self.getButton = QtGui.QPushButton()
		self.getButton.setText("Get")
		self.buttonBox.addButton(self.getButton, QtGui.QDialogButtonBox.ActionRole)

		self.closeButton = QtGui.QPushButton()
        	self.closeButton.setText("Close")
        	self.buttonBox.addButton(self.closeButton, QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.getButton, QtCore.SIGNAL("clicked()"), self.getWorkflow)
		QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), self.closeWindow)
		
		wf_list_sh = subprocess.Popen([self.home_path + '/.qgis2/python/plugins/github_dnl_wf_list.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                wf_list_sh.wait()

		with open(self.home_path + '/wois-workflow-share/wf_names_list') as f:
	        	self.wf_names = f.read().splitlines()
		f.close()
		with open(self.home_path + '/wois-workflow-share/wf_list') as f:
                        self.wf_files = f.read().splitlines()
		f.close()

		self.searchBox = QtGui.QLineEdit()
		self.searchBox.textChanged.connect(self.fillAlgorithmTree)
		self.verticalLayout.addWidget(self.searchBox)
		self.algorithmTree = QtGui.QTreeWidget()
		self.algorithmTree.setHeaderHidden(True)
		self.fillAlgorithmTree()
		self.verticalLayout.addWidget(self.algorithmTree)
		self.algorithmTree.doubleClicked.connect(self.getWorkflow)

		self.algorithmsTab = QtGui.QWidget()
		self.algorithmsTab.setLayout(self.verticalLayout)
		self.tabWidget.addTab(self.algorithmsTab, "Community workflows")
		self.tabWidget.setTabPosition(QtGui.QTabWidget.South)

        	#And the whole layout
        	#==========================

		self.globalLayout = QtGui.QVBoxLayout()
		self.globalLayout.setSpacing(2)
		self.globalLayout.setMargin(0)
		self.globalLayout.addLayout(self.horizontalLayout)
		self.globalLayout.addWidget(self.buttonBox)
		self.setLayout(self.globalLayout)
		QtCore.QMetaObject.connectSlotsByName(self)

    def closeWindow(self):
        self.close()

    # For sharing the workflow
    def getWorkflow(self):
        item = self.algorithmTree.currentItem()
        if isinstance(item, TreeAlgorithmItem):
		wfName = item.wf
		share_ask = 'Are you sure you want to add the selected workflow to your WOIS?'
		reply = QMessageBox.question(self, 'Get WOIS Workflows', share_ask, QMessageBox.Yes, QMessageBox.No)
		if reply == QMessageBox.Yes:
			for i in range(0, len(self.wf_names)):
				if self.wf_names[i] == wfName:
					git_sh = subprocess.Popen([self.home_path + '/.qgis2/python/plugins/github_dnl_wf_file.sh', self.wf_files[i], self.workflows_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                        git_sh.wait()
					wf_added = 0
					for wf_file in glob.glob(self.workflows_path + "/*.workflow"):
						if os.path.basename(wf_file) == self.wf_files[i]:
							wf_added = 1
							QMessageBox.information(self, 'Get WOIS Workflows', 'Workflow added to WOIS with success.', QMessageBox.Ok)
							shutil.rmtree(self.home_path + '/wois-workflow-share')
					if wf_added == 0:
						QMessageBox.warning(self, 'Get WOIS Workflows', 'Workflow not added to your WOIS.', QMessageBox.Ok)
						shutil.rmtree(self.home_path + '/wois-workflow-share')
	else:
		QMessageBox.warning(self, "Warning", "Select a workflow to add to your WOIS.", QMessageBox.Ok);


    # List all the available community WOIS workflows
    def fillAlgorithmTree(self):
        self.algorithmTree.clear()
        text = unicode(self.searchBox.text())

	allAlgs = Processing.algs
        providers = {}
        for provider in Processing.providers:
            providers[provider.getName()] = provider
        for providerName in [self.workflowProvider.getName()]:
            groups = {}
            provider = allAlgs[providerName]
            algs = provider.values()

	    groupItem = QtGui.QTreeWidgetItem()
            groupItem.setText(0, "Shared workflows")
            groups["Shared workflows"] = groupItem
            #add workflows
            for wf in self.wf_names:
                if text == "" or text.lower() in wf.lower():
 	        	wfItem = TreeAlgorithmItem(wf)
        	        groupItem.addChild(wfItem)

            if len(groups) > 0:
                providerItem = QtGui.QTreeWidgetItem()
                providerItem.setText(0, providers[providerName].getDescription())
                providerItem.setIcon(0, providers[providerName].getIcon())
                for groupItem in groups.values():
                    providerItem.addChild(groupItem)
                self.algorithmTree.addTopLevelItem(providerItem)
                providerItem.setExpanded(True)
                for groupItem in groups.values():
                    if text != "":
                        groupItem.setExpanded(True)

        self.algorithmTree.sortItems(0, QtCore.Qt.AscendingOrder)


class TreeAlgorithmItem(QtGui.QTreeWidgetItem):

    def __init__(self, wf):
        QtGui.QTreeWidgetItem.__init__(self)
        self.wf = wf
        self.setText(0, self.wf)
