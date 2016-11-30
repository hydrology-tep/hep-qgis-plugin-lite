# -*- coding: utf-8 -*-

"""
***************************************************************************
    ExportModelDialog.py
    ---------------------
    Date                 : April 2016
    Copyright            : (C) 20126 by DEIMOS Engenharia
    Email                : 
***************************************************************************
*                                                                         *
*                                                                         *
***************************************************************************
"""

__author__ = 'João Andrade'
__date__ = 'April 2016'
__copyright__ = '(C) 2016, DEIMOS Engenharia'

__revision__ = '$Format:%H$'

import codecs
import sys
import os

from PyQt4.QtCore import Qt, QRectF, QMimeData, QPoint, QPointF, QSettings
from PyQt4.QtGui import QDialog, QGraphicsView, QTreeWidget, QIcon, QMessageBox, QFileDialog, QImage, QPainter, QTreeWidgetItem, QFileDialog
from qgis.core import QgsApplication
from processing.core.ProcessingConfig import ProcessingConfig
from processing.core.GeoAlgorithm import GeoAlgorithm
from processing.core.ProcessingLog import ProcessingLog
from processing.gui.HelpEditionDialog import HelpEditionDialog
from processing.gui.AlgorithmDialog import AlgorithmDialog
from processing.gui.AlgorithmClassification import AlgorithmDecorator
from processing.modeler.ModelerAlgorithm import ModelerAlgorithm, ModelerParameter
from processing.modeler.ModelerUtils import ModelerUtils
from processing.modeler.ModelerScene import ModelerScene
from processing.modeler.WrongModelException import WrongModelException
from processing.ui.ui_DlgExportModel import ui_DlgExportModel
from os.path import expanduser
import processing.resources_rc
import subprocess
import fnmatch
import io, json, re, pipes

class ExportModelDialog(QDialog, ui_DlgExportModel):

    USE_CATEGORIES = '/Processing/UseSimplifiedInterface'
    CANVAS_SIZE = 2000

    def __init__(self, alg=None):
        QDialog.__init__(self)

        self.setupUi(self)

        self.zoom = 1

        self.setWindowFlags(Qt.WindowMinimizeButtonHint |
                            Qt.WindowMaximizeButtonHint |
                            Qt.WindowCloseButtonHint)

        self.tabWidget.setCurrentIndex(0)
	self.scene = ModelerScene(self)
        self.scene.setSceneRect(QRectF(0, 0, self.CANVAS_SIZE, self.CANVAS_SIZE))

	self.home_path = expanduser("~")
	self.models_path = self.home_path + "/.qgis2/processing/models"

        def _mimeDataAlgorithm(items):
            item = items[0]
            if isinstance(item, TreeAlgorithmItem):
                mimeData = QMimeData()
                mimeData.setText(item.alg.commandLineName())
            return mimeData

        self.algorithmTree.mimeData = _mimeDataAlgorithm

        # Set button text

	self.btnExport.setText('Export to TEP')

        # Fill trees with models

        self.fillAlgorithmTree()

        if hasattr(self.searchBox, 'setPlaceholderText'):
            self.searchBox.setPlaceholderText(self.tr('Search...'))

        # Connect signals and slots

        self.searchBox.textChanged.connect(self.fillAlgorithmTree)
        self.algorithmTree.doubleClicked.connect(self.exportModel)

        self.btnExport.clicked.connect(self.exportModel)

        if alg is not None:
            self.alg = alg
            self.textGroup.setText(alg.group)
            self.textName.setText(alg.name)
            self.repaintModel()
        else:
            self.alg = ModelerAlgorithm()
            self.alg.ExportModelDialog = self

        self.help = None
        # Indicates whether to update or not the toolbox after
        # closing this dialog
        self.update = False

        self.hasChanged = False


    def exportModel(self):
		item = self.algorithmTree.currentItem()
		if isinstance(item, TreeAlgorithmItem):
			export_ask = "Are you sure you want to export the model to TEP?"
			reply = QMessageBox.question(self, 'Export Models', export_ask, QMessageBox.Yes, QMessageBox.No)
			if reply == QMessageBox.Yes:
				algName = item.alg.commandLineName()[8:]
				for root, dirnames, filenames in os.walk(self.models_path):
					for filename in fnmatch.filter(filenames, '*.model'):
						modelName = os.path.splitext(filename)[0].lower()
						if modelName == algName:
							return_value = self.export_process(self.home_path, root, filename)
							if return_value == 1:
								QMessageBox.information(self, 'Info Message', 'Model already exists on HEP.', QMessageBox.Ok)
							elif return_value == 0:
								QMessageBox.information(self, 'Info Message', 'Model uploaded with success.', QMessageBox.Ok)
		else:
			QMessageBox.warning(self, "Warning", "Select a model to export.", QMessageBox.Ok);

    def fillAlgorithmTree(self):
        self.fillAlgorithmTreeUsingProviders()
        self.algorithmTree.sortItems(0, Qt.AscendingOrder)
        text = unicode(self.searchBox.text())
        if text != '':
			self.algorithmTree.expandAll()

    def fillAlgorithmTreeUsingProviders(self):
        self.algorithmTree.clear()
        text = unicode(self.searchBox.text())
        allAlgs = ModelerUtils.allAlgs
        for providerName in allAlgs.keys():
	  if providerName == 'model':
            groups = {}
            provider = allAlgs[providerName]
            algs = provider.values()

            # Add algorithms
            for alg in algs:
                if not alg.showInModeler or alg.allowOnlyOpenedLayers:
                    continue
                if text == '' or text.lower() in alg.name.lower():
                    if alg.group in groups:
       	                groupItem = groups[alg.group]
               	    else:
                       	groupItem = QTreeWidgetItem()
                       	groupItem.setText(0, alg.group)
                        groupItem.setToolTip(0, alg.group)
       	                groups[alg.group] = groupItem
               	    algItem = TreeAlgorithmItem(alg)
               	    groupItem.addChild(algItem)

            if len(groups) > 0:
                providerItem = QTreeWidgetItem()
                providerItem.setText(0,
                        ModelerUtils.providers[providerName].getDescription())
                providerItem.setToolTip(0,
                        ModelerUtils.providers[providerName].getDescription())
                providerItem.setIcon(0,
                        ModelerUtils.providers[providerName].getIcon())
                for groupItem in groups.values():
                    providerItem.addChild(groupItem)
                self.algorithmTree.addTopLevelItem(providerItem)
                providerItem.setExpanded(text != '')
                for groupItem in groups.values():
                    if text != '':
                        groupItem.setExpanded(True)

        self.algorithmTree.sortItems(0, Qt.AscendingOrder)


    def generate_conf_file(self, conf_file, in_params, out_params, upload_to_tep):
	model_id = os.path.splitext(os.path.basename(conf_file))[0]
	f = open(conf_file, 'w')
	confStr = '''"""
The ultimate process to test the status and update capabilities of the server
The processes shoul be requested as follows:
../wps.py?request=execute
&service=wps
&version=1.0.0
&identifier=hello
&status=true
&storeExecuteResponse=true
"""

from pywps.Process import WPSProcess
class Process(WPSProcess):
    def __init__(self):
	WPSProcess.__init__(self,
			    identifier = "''' + model_id + '''",
			    version = "1.0.0",
			    title = "''' + self.model_name + '''",
			    storeSupported = "true",
			    statusSupported = "true",
			    abstract="",
			    grassLocation =False)
'''
	f.write(confStr)
	paramsIn = []
	paramsOut = []
	complex_inputs = []
	for i in range(len(in_params)):
		if in_params[i][0] == "ParameterBoolean":
			f.write('\n' + '	self.inParam' + str(i) + ' = self.addLiteralInput(identifier="' + in_params[i][1] + '", title="' + in_params[i][2] + '", type=type(False), default=' + str(in_params[i][3]) + ', allowedValues = [True, False])')
		elif in_params[i][0] == "ParameterNumber":
			if in_params[i][3] == 'true':
				f.write('\n' + '	self.inParam' + str(i) + ' = self.addLiteralInput(identifier="' + in_params[i][1] + '", title="' + in_params[i][2] + '", default=' + str(in_params[i][4]) + ')')
			else:
				f.write('\n' + '	self.inParam' + str(i) + ' = self.addLiteralInput(identifier="' + in_params[i][1] + '", title="' + in_params[i][2] + '", type=type(0.0), default=' + str(in_params[i][4]) + ')')
		elif in_params[i][0] == "ParameterString":
			f.write('\n' + '	self.inParam' + str(i) + ' = self.addLiteralInput(identifier="' + in_params[i][1] + '", title="' + in_params[i][2] + '", type=type(""), default=' + in_params[i][3] + ')')
		else:
			complex_inputs.append(i)
			f.write('\n' + '	self.inParam' + str(i) + ' = self.addComplexInput(identifier="' + in_params[i][1] + '", title="' + in_params[i][2] + '")')
		paramsIn.append('self.inParam' + str(i))
	for o in range(len(out_params)):
		f.write('\n' + '	self.outputName' + str(o) + ' = self.addLiteralInput(identifier="' + out_params[o][0] + '", title="Name of the output file for: ' + out_params[o][1] + '", type=type(""))')
		paramsOut.append('self.outputName' + str(o))
	if upload_to_tep == 1:
		f.write('\n' + '	self.metadataOut = self.addComplexOutput(identifier="result_metadata", title="Metadata XML URL", formats = [{"mimeType":"application/xml","mimetype":"text/xml"}], asReference=True)')
	
	confStr = '''

    def execute(self):
	import time
	import os, sys
	import subprocess
	import xml.etree.ElementTree as ET
	
	self.status.set("Preparing....", 0)
	time.sleep(2)
	uuid = self.pywps.UUID
	subprocess.Popen(['mkdir', '/var/www/wps/wpsoutputs/' + uuid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	subprocess.Popen(['chmod', '775', '/var/www/wps/wpsoutputs/' + uuid], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
'''
	for i in range(len(complex_inputs)):
		confStr = confStr + '''
	inputfile''' + str(complex_inputs[i]) + ''' = self.inParam''' + str(complex_inputs[i]) + '''.getValue()
	f = open(inputfile''' + str(complex_inputs[i]) + ''', 'r')
	xml = f.read()
	root = ET.fromstring(xml)
	for child in root.findall('{http://www.w3.org/2005/Atom}entry'):
		self.prodURL''' + str(complex_inputs[i]) + ''' = child.find('{http://www.w3.org/2005/Atom}id').text
    	'''
		paramsIn[complex_inputs[i]] = 'self.prodURL' + str(complex_inputs[i])
	f.write(confStr)

	if upload_to_tep == 1:
		confStr = '''
	import socket
	self.ip = socket.gethostname()
	import StringIO
	self.metadataOut.setValue(StringIO.StringIO('<wps:Reference href="http://' + self.ip + '/wpsoutputs/' + uuid + '/metadata.xml" method="GET" mimeType="application/atom+xml" />'))'''
		f.write(confStr)

	confStr = '''
	l=subprocess.Popen(["/var/www/wps/run_model.sh", "''' + model_id + '''"'''

	for i in range(len(in_params)):
		if 'prodURL' in paramsIn[i]:
			confStr = confStr + ', ' + paramsIn[i]
		else:
			confStr = confStr + ', str(' + paramsIn[i] + '.getValue())'
	for o in range(len(out_params)):
		confStr = confStr + ', "/var/www/wps/wpsoutputs/" + uuid + "/" + ' + paramsOut[o] + '.getValue()'
	confStr = confStr + '''],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err =l.communicate()
	print out
	print err
	errcode = l.returncode
	self.status.set("Finished", 0)
'''
	f.write(confStr)
	f.close()


    def read_model_file(self, model_file, conf_file):
	f = open(model_file, 'r')
	model = json.load(f)
	f.close()
	self.model_name = model['values']['name']
	in_params = []
	for input_id in model['values']['inputs']:
		param_type = model['values']['inputs'][input_id]['values']['param']['class'].split('.')[3]
		param_id = input_id.lower()
		param_title = model['values']['inputs'][input_id]['values']['param']['values']['description']
		if param_type == "ParameterBoolean" or param_type == "ParameterString":
			param_default = model['values']['inputs'][input_id]['values']['param']['values']['default']
			in_params.append([param_type, param_id, param_title, param_default])
		elif param_type == "ParameterNumber":
			isInt = model['values']['inputs'][input_id]['values']['param']['values']['isInteger']	
			param_default = model['values']['inputs'][input_id]['values']['param']['values']['default']
			in_params.append([param_type, param_id, param_title, isInt, param_default])
		else:
			in_params.append([param_type, param_id, param_title])
	out_params = []
	upload_to_tep = 0
	for alg_id in model['values']['algs']:
		for output_id in model['values']['algs'][alg_id]['values']['outputs']:
			out_id = 'out' + str(len(out_params))
			out_title = model['values']['algs'][alg_id]['values']['outputs'][output_id]['values']['description']
			out_params.append([out_id, out_title])
		if model['values']['algs'][alg_id]['values']['consoleName'] == "script:uploadtotep":
			upload_to_tep = 1

	self.generate_conf_file(conf_file, in_params, out_params, upload_to_tep)

    def generate_init_file(self, init_file, conf_file):
	model_id = os.path.splitext(os.path.basename(conf_file))[0]
	f = open(init_file, 'r')
	wps_services = f.readline()
	f.close()
	if '"' + model_id + '"' in wps_services:
		pass
	elif len(wps_services) < 12:
		wps_services = '__all__ = ["' + model_id + '"]'
		f = open(init_file, 'w')
		f.write(wps_services)
		f.close()
	elif '[]' in wps_services:
		wps_services = re.sub(']', '"' + model_id + '"]', str(wps_services))
		f = open(init_file, 'w')
		f.write(wps_services)
		f.close()
	else:
		wps_services = re.sub(']', ',"' + model_id + '"]', str(wps_services))
		f = open(init_file, 'w')
		f.write(wps_services)
		f.close()
	

    def export_process(self, home_path, root, filename):

	destModelDir = home_path + "/.qgis2/processing/models/WOIS/"
	destConfDir = "/var/www/wps/processes/"

	model_file = root + '/' + filename
	remote_conf_file = "/var/www/wps/processes/" + os.path.splitext(filename)[0] + ".py"

	if os.path.isfile(remote_conf_file):
		return 1
	else:
		conf_file = home_path + "/.qgis2/python/plugins/processing/tmp/" + os.path.splitext(filename)[0] + ".py"
		self.read_model_file(model_file, conf_file)
		subprocess.call(['cp', '/var/www/wps/processes/__init__.py', home_path + '/.qgis2/python/plugins/processing/tmp/'])
		init_file = home_path + '/.qgis2/python/plugins/processing/tmp/__init__.py'
		self.generate_init_file(init_file, conf_file)
		subprocess.call(['mv', model_file, destModelDir])
		subprocess.call(['mv', home_path + '/.qgis2/python/plugins/processing/tmp/__init__.py', destConfDir])
		subprocess.call(['mv', conf_file, destConfDir])
		subprocess.call(['chmod', '+x', remote_conf_file])
		subprocess.call(['chmod', '+x', destConfDir + '__init__.py'])
		subprocess.call(['sudo', 'service', 'httpd', 'restart'])
		return 0


class TreeAlgorithmItem(QTreeWidgetItem):

    def __init__(self, alg):
        settings = QSettings()
        useCategories = settings.value(ExportModelDialog.USE_CATEGORIES, type=bool)
        QTreeWidgetItem.__init__(self)
        self.alg = alg
        icon = alg.getIcon()
        name = alg.name
        if useCategories:
            icon = GeoAlgorithm.getDefaultIcon()
            (group, subgroup, name) = AlgorithmDecorator.getGroupsAndName(alg)
        self.setIcon(0, icon)
        self.setToolTip(0, name)
        self.setText(0, name)
