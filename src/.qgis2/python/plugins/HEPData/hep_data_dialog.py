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
from PyQt4.QtGui import QAction, QDialog, QGraphicsView, QTreeWidget, QIcon, QMessageBox, QFileDialog, QImage, QPainter, QTreeWidgetItem, QFileDialog
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
import sys, os.path, socket
#import urllib2
import urllib, ssl
import xml.etree.ElementTree as ET

from processing.gui.ToolboxAction import ToolboxAction
from DataTreeDialog import DataTreeDialog

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'hep_data_dialog_base.ui'))


class HEPDataDialog(QtGui.QDialog, FORM_CLASS):
    def __init__(self, url, apikey):
        """Constructor."""
        super(HEPDataDialog, self).__init__()
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
	self.url = url
	self.apikey = apikey
	if hasattr(self.lineEdit, 'setPlaceholderText'):
	    self.lineEdit.setText(self.url)
	if hasattr(self.lineEditAPIKey, 'setPlaceholderText'):
	    if self.apikey == '':
		self.lineEditAPIKey.setPlaceholderText('Insert your API Key')
	    else:
		self.lineEditAPIKey.setText(self.apikey)

	self.button_box.button(QtGui.QDialogButtonBox.Save).setText("Load")
	self.button_box.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.loadDataTree)

    def loadDataTree(self):

	self.datapackages = []
	self.dp_links = []
	context = ssl._create_unverified_context()
	self.allData = []

	try:
		self.url = self.lineEdit.text()
		self.apikey = self.lineEditAPIKey.text()
	        self.finalURL = self.url + '?key=' + self.apikey
		file = urllib.urlopen(self.finalURL, context=context)
		data = file.read()
                file.close()
                root = ET.fromstring(data)
		self.userAPIKeyFilepath = os.path.expanduser("~") + "/.qgis2/python/plugins/HEPData/userAPIKey.txt"
		if os.path.isfile(self.userAPIKeyFilepath):
                        os.remove(self.userAPIKeyFilepath)
                        f = open(self.userAPIKeyFilepath, 'w')
                        f.write(self.apikey)
                        f.close()
		else:
			f = open(self.userAPIKeyFilepath, 'w')
                        f.write(self.apikey)
                        f.close()

		for child in root.findall('{http://www.w3.org/2005/Atom}entry'):
		   self.dp = child.find('{http://www.w3.org/2005/Atom}content').text
    	    	   self.datapackages.append(self.dp)
		   self.allData.append((self.dp, [], []))
		   for link in child.findall('{http://www.w3.org/2005/Atom}link'):
			if link.attrib['rel'] == 'public':
				self.dp_links.append(link.attrib['href'])

		self.dp_counter = 0
		self.host = socket.gethostname()

		for dp_link in self.dp_links:
			file = urllib.urlopen(dp_link, context=context)
			data2 = file.read()
			file.close()
			root2 = ET.fromstring(data2)
			for child in root2.findall('{http://www.w3.org/2005/Atom}entry'):
				self.prodName = child.find('{http://purl.org/dc/elements/1.1/}identifier').text
				self.allData[self.dp_counter][1].append(self.prodName)
				### Updated ###
				self.prodURL = child.find('{http://www.w3.org/2005/Atom}id').text + '&do=' + self.host
				file2 = urllib.urlopen(self.prodURL, context=context)
				data3 = file2.read()
				file2.close()
				root3 = ET.fromstring(data3)
				block_first = 0
				for entry in root3.findall('{http://www.w3.org/2005/Atom}entry'):
					for link in entry.findall('{http://www.w3.org/2005/Atom}link'):
						if link.attrib['rel'] == 'enclosure' and block_first == 0:
							block_first = 1
							self.allData[self.dp_counter][2].append(link.attrib['href'])
				####
			self.dp_counter += 1

		#Launch Dialog
		dlg = DataTreeDialog(self, self.allData, self.url, self.apikey)
		dlg.exec_()

    	except ValueError:
		self.relaunch_config()
	except ET.ParseError:
		self.relaunch_config()
	except IOError:
		self.relaunch_config()

    def relaunch_config(self):
	QMessageBox.warning(self, "Warning", "Invalid URL.", QMessageBox.Ok);
	self.url = "https://hydrology-tep.eo.esa.int/t2api/data/package/search"
	self.apikey = self.lineEditAPIKey.text()
	self.dlg = HEPDataDialog(self.url, self.apikey)
	self.dlg.exec_()
