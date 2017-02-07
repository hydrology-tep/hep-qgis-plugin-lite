"""
***************************************************************************
   WorkflowShareDialog.py
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
import fnmatch, re, subprocess

# Dialog for sharing workflows
class WorkflowShareDialog(AlgorithmDialogBase):
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
		self.setWindowTitle("Share WOIS Workflow")
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

		self.shareButton = QtGui.QPushButton()
		self.shareButton.setText("Share")
		self.buttonBox.addButton(self.shareButton, QtGui.QDialogButtonBox.ActionRole)

		self.closeButton = QtGui.QPushButton()
        	self.closeButton.setText("Close")
        	self.buttonBox.addButton(self.closeButton, QtGui.QDialogButtonBox.ActionRole)

		QtCore.QObject.connect(self.shareButton, QtCore.SIGNAL("clicked()"), self.shareWorkflow)
		QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL("clicked()"), self.closeWindow)
		
		
		self.searchBox = QtGui.QLineEdit()
		self.searchBox.textChanged.connect(self.fillAlgorithmTree)
		self.verticalLayout.addWidget(self.searchBox)
		self.algorithmTree = QtGui.QTreeWidget()
		self.algorithmTree.setHeaderHidden(True)
		self.fillAlgorithmTree()
		self.verticalLayout.addWidget(self.algorithmTree)
		self.algorithmTree.doubleClicked.connect(self.shareWorkflow)

		self.algorithmsTab = QtGui.QWidget()
		self.algorithmsTab.setLayout(self.verticalLayout)
		self.tabWidget.addTab(self.algorithmsTab, "Workflows")
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
    def shareWorkflow(self):
        item = self.algorithmTree.currentItem()
        if isinstance(item, TreeAlgorithmItem):
		algName = item.alg.commandLineName()[9:]
		share_ask = 'Are you sure you want to share the selected workflow?'
		reply = QMessageBox.question(self, 'Share WOIS Workflows', share_ask, QMessageBox.Yes, QMessageBox.No)
		if reply == QMessageBox.Yes:
			for root, dirnames, filenames in os.walk(self.workflows_path):
				for filename in fnmatch.filter(filenames, '*.workflow'):
					wf_file = root + '/' + filename
					with open(wf_file,"r") as f:
						workflowName = f.readline()[6:]
						wf_name = re.sub('[^0-9a-zA-Z]+', '', workflowName).lower()
					if wf_name == algName:
						git_sh = subprocess.Popen([self.home_path + '/.qgis2/python/plugins/github_upload.sh', wf_file, workflowName], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
						git_sh.wait()
						if os.path.isfile(self.home_path + '/wois-workflow-share/name_repeated'):
							QMessageBox.warning(self, 'Share WOIS Workflows', 'Workflow share failed. A workflow with the same name already exists.', QMessageBox.Ok)
                                                	shutil.rmtree(self.home_path + '/wois-workflow-share')
						elif os.path.isfile(self.home_path + '/wois-workflow-share/file_repeated'):
                                                        QMessageBox.warning(self, 'Share WOIS Workflows', 'Workflow share failed. Workflow file already exists.', QMessageBox.Ok)
                                                        shutil.rmtree(self.home_path + '/wois-workflow-share')
						elif os.path.isfile(self.home_path + '/wois-workflow-share/' + filename):
							QMessageBox.information(self, 'Share WOIS Workflows', 'Workflow shared with success.', QMessageBox.Ok)
							shutil.rmtree(self.home_path + '/wois-workflow-share')
						else:
							QMessageBox.warning(self, 'Share WOIS Workflows', 'Workflow share failed.', QMessageBox.Ok)
							shutil.rmtree(self.home_path + '/wois-workflow-share')

	else:
		QMessageBox.warning(self, "Warning", "Select a workflow to share.", QMessageBox.Ok);


    # List all the available TIGER-NET workflows
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
            #add algorithms
            for alg in algs:
                if text == "" or text.lower() in alg.name.lower():
                    if alg.group in groups:
                        groupItem = groups[alg.group]
                    else:
                        groupItem = QtGui.QTreeWidgetItem()
                        groupItem.setText(0, alg.group)
                        groups[alg.group] = groupItem
                    algItem = TreeAlgorithmItem(alg)
                    groupItem.addChild(algItem)

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

    def __init__(self, alg):
        QtGui.QTreeWidgetItem.__init__(self)
        self.alg = alg
        self.setText(0, alg.name)
        self.setIcon(0, alg.getIcon())
