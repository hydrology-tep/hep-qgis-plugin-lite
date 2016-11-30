# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HEPDataDialog
                                 A QGIS plugin
 This plugin allows to get Data from HEP
                             -------------------
        begin                : 2016-05-23
        git sha              : $Format:%H$
        copyright            : (C) 2016 by DEIMOS Engenharia
        email                : joao.andrade@deimos.com.pt
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication, Qt, QRectF, QMimeData, QPoint, QPointF, QSettings
from PyQt4.QtGui import QAction, QDialog, QGraphicsView, QTreeWidget, QIcon, QMessageBox, QFileDialog, QImage, QPainter, QTreeWidgetItem, QFileDialog, QLabel
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
import sys, os.path, socket
#import urllib2
import urllib, ssl
import xml.etree.ElementTree as ET

from processing.core.Processing import Processing
from processing.gui.CommanderWindow import CommanderWindow
from processing.modeler.ExportModelAction import ExportModelAction
from processing.gui.ToolboxAction import ToolboxAction
from processing_workflow.ProcessingWorkflowPlugin import ProcessingWorkflowPlugin
from processing_workflow.WorkflowProvider import WorkflowProvider
from processing_workflow.ShareWorkflowAction import ShareWorkflowAction

#from hep_data import HEPData
from hep_data_dialog import HEPDataDialog


class HEPGenDialog():
    def __init__(self,iface):
        """Constructor."""
	self.dialog = QtGui.QDialog()
	self.dialog.setWindowTitle("Hydrology-TEP")
	self.iface=iface
	self.dialog.setFixedSize(410, 170)

	self.btn1 = QtGui.QPushButton('Get Data from TEP',self.dialog)
	self.btn1.setIcon(QIcon(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/dnl.png'))
	self.btn1.move(10,10)
	self.btn1.setStyleSheet("padding-left: 10px; padding-top: 2px; padding-bottom: 2px; text-align: left")
	self.btn1.setFixedWidth(180)
	self.btn1.clicked.connect(self.getData)
	self.btn2 = QtGui.QPushButton('Upload Data to TEP', self.dialog)
	self.btn2.setIcon(QIcon(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/upl.png'))
	self.btn2.move(10,50)
	self.btn2.setStyleSheet("padding-left: 10px; padding-top: 2px; padding-bottom: 2px; text-align: left")
	self.btn2.setFixedWidth(180)
	self.btn2.clicked.connect(self.uploadTEP)
	self.btn3 = QtGui.QPushButton('Export model to TEP', self.dialog)
        self.btn3.setIcon(QIcon(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/exp.png'))
        self.btn3.move(10,90)
	self.btn3.setStyleSheet("padding-left: 10px; padding-top: 2px; padding-bottom: 2px; text-align: left")
	self.btn3.setFixedWidth(180)
        self.btn3.clicked.connect(self.exportModel)
	self.btn4 = QtGui.QPushButton('Share WOIS workflow', self.dialog)
	self.btn4.setIcon(QIcon(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/share.png'))
	self.btn4.move(10,130)
	self.btn4.setStyleSheet("padding-left: 10px; padding-top: 2px; padding-bottom: 2px; text-align: left")
	self.btn4.setFixedWidth(180)
	self.btn4.clicked.connect(self.shareWorkflow)
	self.hep_image = QtGui.QLabel(self.dialog)
	self.pixmap = QtGui.QPixmap(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/hep_main_img.png')
	self.pixmap.scaledToWidth(261)
	self.pixmap.scaledToHeight(67)
	self.hep_image.setPixmap(self.pixmap)
	self.hep_image.move(200,47)
	self.consortium = QtGui.QLabel(self.dialog)
	self.pm_consortium = QtGui.QPixmap(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/consortium.png')
	self.pm_consortium.scaledToWidth(100)
	self.pm_consortium.scaledToHeight(57)
	self.consortium.setPixmap(self.pm_consortium)
	self.consortium.move(200,135)
	self.dialog.exec_()


    def uploadTEP(self):
	alg = Processing.getAlgorithm("script:uploadtotep")
	cw = CommanderWindow(self.iface.mainWindow(), self.iface.mapCanvas())
	self.dialog.hide()
	if alg is not None:
		cw.runAlgorithm(alg)

    def shareWorkflow(self):
	self.dialog.hide()
	self.dlg = ProcessingWorkflowPlugin(self.iface)
	self.dlg2 = WorkflowProvider(self.dlg.iface)
	self.dlg2.openShareWorkflow()

    def exportModel(self):
	self.dialog.hide()
	self.dlg = ExportModelAction()
	self.dlg.execute()

    def getData(self):
	self.dialog.hide()

	#self.url = "https://tep-hydro-dev.terradue.com/t2api/data/package/search"
        self.url = "https://hydrology-tep.eo.esa.int/t2api/data/package/search"
        self.apikey = ''
        self.userAPIKeyFilepath = os.path.expanduser("~") + "/.qgis2/python/plugins/HEPPlugin/userAPIKey.txt"
        if os.path.isfile(self.userAPIKeyFilepath):
                f = open(self.userAPIKeyFilepath, 'r')
                self.apikey = f.read()
                f.close()
                self.dlg = HEPDataDialog(self.url, self.apikey)
                self.dlg.loadDataTree()
        else:
                self.dlg = HEPDataDialog(self.url, self.apikey)
                self.dlg.exec_()

