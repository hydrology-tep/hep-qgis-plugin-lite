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

from processing.modeler.ExportModelAction import ExportModelAction
from processing.gui.ToolboxAction import ToolboxAction


class HEPGenDialog():
    def __init__(self,iface):
        """Constructor."""
	self.dialog = QtGui.QDialog()
	self.dialog.setWindowTitle("Hydrology-TEP")
	self.iface=iface
	self.dialog.setFixedSize(410, 80)

	self.btn = QtGui.QPushButton('Export model to TEP', self.dialog)
        self.btn.setIcon(QIcon(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/exp.png'))
        self.btn.move(10,15)
	self.btn.setStyleSheet("padding-top: 2px; padding-bottom: 2px; text-align: center")
	self.btn.setFixedWidth(180)
        self.btn.clicked.connect(self.exportModel)
	self.hep_image = QtGui.QLabel(self.dialog)
	self.pixmap = QtGui.QPixmap(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/hep_main_img.png')
	self.pixmap.scaledToWidth(261)
	self.pixmap.scaledToHeight(67)
	self.hep_image.setPixmap(self.pixmap)
	self.hep_image.move(200,8)
        self.consortium = QtGui.QLabel(self.dialog)
        self.pm_consortium = QtGui.QPixmap(os.path.expanduser('~') + '/.qgis2/python/plugins/HEPPlugin/images/consortium.png')
        self.pm_consortium.scaledToWidth(80)
        self.pm_consortium.scaledToHeight(57) 
        self.consortium.setPixmap(self.pm_consortium)
        self.consortium.move(10,48)
	self.dialog.exec_()

    def exportModel(self):
	self.dialog.hide()
	self.dlg = ExportModelAction()
	self.dlg.execute()

