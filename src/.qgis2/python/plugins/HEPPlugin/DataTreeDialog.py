# -*- coding: utf-8 -*-

"""
***************************************************************************
    DataTreeDialog.py
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

from PyQt4.QtCore import Qt, QRectF, QMimeData, QPoint, QPointF, QSettings, QByteArray
from PyQt4.QtGui import QDialog, QGraphicsView, QTreeWidget, QIcon, QMessageBox, QFileDialog, QImage, QPainter, QTreeWidgetItem, QFileDialog, QLabel, QApplication, QWidget, QProgressBar, QMovie, QProgressDialog
from qgis.core import QgsApplication
from processing.core.GeoAlgorithm import GeoAlgorithm
from processing.modeler.ModelerAlgorithm import ModelerAlgorithm, ModelerParameter
from processing.modeler.ModelerUtils import ModelerUtils
from processing.modeler.ModelerScene import ModelerScene
from ui_DlgDataTree import ui_DlgDataTree
import subprocess, shutil
import fnmatch
import platform
import time
from threading import Thread

class DataTreeDialog(QDialog, ui_DlgDataTree):

    USE_CATEGORIES = '/Processing/UseSimplifiedInterface'
    CANVAS_SIZE = 2000

    def __init__(self, parent, data, url, apikey):
        QDialog.__init__(self)

        self.setupUi(self)

        self.zoom = 1

        self.setWindowFlags(Qt.WindowMinimizeButtonHint |
                            Qt.WindowMaximizeButtonHint |
                            Qt.WindowCloseButtonHint)

        self.tabWidget.setCurrentIndex(0)
	self.scene = ModelerScene(self)
        self.scene.setSceneRect(QRectF(0, 0, self.CANVAS_SIZE, self.CANVAS_SIZE))

	self.parent = parent
	self.allData = data
	self.url = url
	self.apikey = apikey

        def _mimeDataAlgorithm(items):
            item = items[0]
            if isinstance(item, TreeDataItem):
                mimeData = QMimeData()
                mimeData.setText(item.alg.commandLineName())
            return mimeData

        self.dataTree.mimeData = _mimeDataAlgorithm

	# Set button "Download"

	self.btnDownload.setText('Get Data')
	self.btnDownload.clicked.connect(self.downloadData)

	self.btnConfig.setText('Config')
	self.btnConfig.clicked.connect(self.configURL)

        # Fill trees with data

        self.fillDataTree()

        if hasattr(self.searchBox, 'setPlaceholderText'):
            self.searchBox.setPlaceholderText(self.tr('Search...'))

        # Connect signals and slots

        self.searchBox.textChanged.connect(self.fillDataTree)
        self.dataTree.doubleClicked.connect(self.downloadData)
	self.progressBar.hide()

	self.cacheLabelSpace = QLabel()
	self.verticalLayout.addWidget(self.cacheLabelSpace)
	self.cacheLabel = QLabel()
	self.verticalLayout.addWidget(self.cacheLabel)
	self.cacheLabel.setText("Caching Data... (this operation can take a few minutes)")
	#self.movie = QMovie("/home/woisuser/.qgis2/python/plugins/HEPData/loading.gif", QByteArray(), self)
	#self.movie.setCacheMode(QMovie.CacheNone) 
       	#self.movie.setSpeed(100) 
       	#self.cacheLabelMovie.setMovie(self.movie)
	#self.movie.start()
	self.cacheLabelSpace.hide()
	self.cacheLabel.hide()

        self.help = None
        # Indicates whether to update or not the toolbox after
        self.update = False
        self.hasChanged = False

    def downloadData(self, q):
	self.saveDir = ""
	size = 0
        new_files = []
        to_download = []
        not_downloaded = []
        already_exists = []
	item = self.dataTree.currentItem()
	if isinstance(item, TreeDataItem):
		self.saveDir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		if self.saveDir == "":
			return

		for dp in self.allData:
			for i in range(len(dp[1])):
				if dp[1][i] == item.text(0):
					os.system("curl -vs " + dp[2][i] +  " 2> /tmp/verbose.txt")
					with open("/tmp/verbose.txt") as f:
						verbose = f.readlines()
					for line in verbose:
						if 'Location' in line:
							file_location = line[12:-1]
					f.close()
					os.system("rm /tmp/verbose.txt")
					new_file = self.saveDir + '/' + os.path.basename(file_location).rstrip("\r")
					if os.path.isfile(new_file):
						QMessageBox.information(self, 'Info Message', 'Product "' + dp[1][i] + '" already exists at ' + self.saveDir, QMessageBox.Ok)
						return

					#os.system("wget --spider " + file_location + " 2>&1 | grep Length | awk '{print $2}' > /tmp/size.txt")
					cmd = None
					cmd = subprocess.Popen(["wget", "--spider", file_location], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
					time.sleep(0.5)
					if cmd.poll() is None:
						#self.cacheLabelSpace.show()
                                                #self.cacheLabel.show()
					        w = QWidget()
						box = QMessageBox(w)
                                                box.setIcon(QMessageBox.Information)
                                                box.setWindowTitle('Info Message')
                                                box.setText('Product "' + dp[1][i] + '" is being cached. It can take some time.')
                                                box.setStandardButtons(QMessageBox.Ok)
                                                buttonY = box.button(QMessageBox.Ok)
                                                buttonY.setText('Download product later')
                                                box.exec_()
						#box = QMessageBox()
						#box.setIcon(QMessageBox.Question)
						#box.setWindowTitle('Info Message')
						#box.setText('Product selected is not on the cache. It can take some time. Wait or come back later?')
						#box.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
						#buttonY = box.button(QMessageBox.Yes)
						#buttonY.setText('Wait')
						#buttonN = box.button(QMessageBox.No)
						#buttonN.setText('Come back later')
						#box.exec_()
                           
						if box.clickedButton() == buttonY:
							return
						#	 cmd_out = cmd.communicate()[1].split(" ")
		                                #        for part in range(len(cmd_out)):
        	        	                #                if "Length" in cmd_out[part]:
	                        	        #                        size=cmd_out[part+1]
		                                       
		                                #        self.cacheLabelSpace.hide()
                		                #        self.cacheLabel.hide()
                                		#        w = QWidget()
		                                #        QMessageBox.information(w, 'Info Message', 'Product "' +dp[1][i] + '" was cached with success. Press OK to start download.', QMessageBox.Ok)
		                                #        for part in range(len(cmd_out)):
                		                #                if "Length" in cmd_out[part]:
                                		#                        size=cmd_out[part+1]
		                                #        os.chdir(self.saveDir)
                		                #        subprocess.Popen(['wget', '--content-disposition', dp[2][i]])
                                		#        self.progressBar.show()
                                        	#	current_size = 0
		                                #        progress = 0
                		                #        while progress < 100:
                                		#                try:
                                                #		        current_size = int(os.stat(new_file).st_size)
		                                #                        progress = int((float(current_size)/float(size))*100)
                		                #                        self.progressBar.setValue(progress)
                                		#                except Exception:
                                                #		        pass
		                                #        QMessageBox.information(self, 'Info Message', 'Product "' + dp[1][i] + '" downloaded with success.', QMessageBox.Ok)
                		                #        self.progressBar.setValue(0)
                                		#        self.progressBar.hide()
		                                #        return      
						#elif box.clickedButton() == buttonN:
						#	self.cacheLabelSpace.hide()
                                                #       self.cacheLabel.hide()
						#	return

					cmd_out = cmd.communicate()[1].split(" ")
                                        for part in range(len(cmd_out)):
	                                        if "Length" in cmd_out[part]:
        	                                        size=cmd_out[part+1]
					os.chdir(self.saveDir)
					subprocess.Popen(['wget', '--content-disposition', dp[2][i]])
					self.progressBar.show()
					current_size = 0
					progress = 0
					while progress < 100:
						try:
							current_size = int(os.stat(new_file).st_size)
							progress = int((float(current_size)/float(size))*100)
							self.progressBar.setValue(progress)
						except Exception:
							pass
					QMessageBox.information(self, 'Info Message', 'Product "' + dp[1][i] + '" downloaded with success.', QMessageBox.Ok)
					self.progressBar.setValue(0)
					self.progressBar.hide()
					return		
	elif isinstance(item, QTreeWidgetItem):
		self.saveDir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
		if self.saveDir == "":
                        return
                for dp in self.allData:
			if dp[0] == item.text(0):
				if not os.path.isdir(self.saveDir + "/" + dp[0]):
					os.mkdir(self.saveDir + "/" + dp[0])
				size = 0
				new_files = []
				to_download = []
				not_downloaded = []
				already_exists = []
				for i in range(len(dp[1])):
					os.system("curl -vs " + dp[2][i] +  " 2> /tmp/verbose.txt")
               	                        with open("/tmp/verbose.txt") as f:
                       	                        verbose = f.readlines()
                       	                for line in verbose:
                           			if 'Location' in line:
                          	                	file_location = line[12:-1]
                               	        f.close()
                               	        os.system("rm /tmp/verbose.txt")
					cmd = None
					cmd = subprocess.Popen(["wget", "--spider", file_location], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                                        time.sleep(1)
					
					if cmd.poll() is None:
						not_downloaded.append(dp[1][i])
                                                w = QWidget()
                                                box = QMessageBox()
                                                box.setIcon(QMessageBox.Information)
                                                box.setWindowTitle('Info Message')
                                                box.setText('Product "' + dp[1][i] + '" is being cached. It can take some time.')
                                                box.setStandardButtons(QMessageBox.Ok)
                                                buttonY = box.button(QMessageBox.Ok)
                                                buttonY.setText('Download product later')
                                                box.exec_()
					else:
						if os.path.isfile(self.saveDir + '/' + dp[0] + '/' + os.path.basename(file_location).rstrip("\r")):
							already_exists.append(dp[1][i])
						else:
							new_files.append(self.saveDir + '/' + dp[0] + '/' + os.path.basename(file_location).rstrip("\r"))
                                                        to_download.append(dp[2][i])
                                                        cmd_out = cmd.communicate()[1].split(" ")
                                                        for part in range(len(cmd_out)):
                                                                if "Length" in cmd_out[part]:
                                                                        size = size + float(cmd_out[part+1])
                	                #os.system("wget --spider " + file_location + " 2>&1 | grep Length | awk '{print $2}' > /tmp/size.txt")

                               	if len(already_exists) == len(dp[1]):
					QMessageBox.information(self, 'Info Message', 'Data package "' + dp[0] + '" already exists at ' + self.saveDir, QMessageBox.Ok)
					return
				elif len(not_downloaded) == len(dp[1]):
                                        QMessageBox.information(self, 'Info Message', 'Products of data package "' + dp[0] + '" are being cached. Download the data package or the products later.', QMessageBox.Ok)
					return
				elif (len(already_exists) + len(not_downloaded)) == len(dp[1]):
					QMessageBox.information(self, 'Info Message', 'Some products already exist and other products are being cached. Download missing products later.', QMessageBox.Ok)
                                        return
				os.chdir(self.saveDir + "/" + dp[0])
				for i in range(len(to_download)):
	       				subprocess.Popen(['wget', '--content-disposition', to_download[i]])
				self.progressBar.show()
                       	        progress = 0
				while progress < 100:
					try:
						current_size = 0
						for i in range(len(new_files)):
							current_size = current_size + int(os.stat(new_files[i]).st_size)
                               	                progress = int((float(current_size)/float(size))*100)
                               	                self.progressBar.setValue(progress)
					except Exception:
						pass
				if len(not_downloaded) != 0:
					QMessageBox.information(self, 'Info Message', 'Data package "' + dp[0] + '" partially downloaded. Download missing products later.', QMessageBox.Ok)
				else:
					QMessageBox.information(self, 'Info Message', 'Data package "' + dp[0] + '" downloaded with success.', QMessageBox.Ok)
				self.progressBar.setValue(0)
                                self.progressBar.hide()
				return
	else:
		QMessageBox.warning(self, "Warning", "Select a product or a Data package to download.", QMessageBox.Ok);

    def configURL(self):
	self.parent.show()
	self.close()

    def fillDataTree(self):
        self.fillDataTreeUsingProviders()
        self.dataTree.sortItems(0, Qt.AscendingOrder)
        text = unicode(self.searchBox.text())
        if text != '':
            self.dataTree.expandAll()


    def fillDataTreeUsingProviders(self):
        self.dataTree.clear()
        text = unicode(self.searchBox.text())

        groups = {}

        for dp in self.allData:
		groupItem = QTreeWidgetItem()
        	groupItem.setText(0, dp[0])
        	groupItem.setToolTip(0, dp[0])
       		groups[dp[0]] = groupItem
		for prod in dp[1]:
			if text == '' or text.lower() in prod.lower():
	        	      	prodItem = TreeDataItem(prod)
        		       	groupItem.addChild(prodItem)
        		    	if len(groups) > 0:
                	        	self.dataTree.addTopLevelItem(groupItem)
        self.dataTree.sortItems(0, Qt.AscendingOrder)


class TreeDataItem(QTreeWidgetItem):

    def __init__(self, prod):
        settings = QSettings()
        useCategories = settings.value(DataTreeDialog.USE_CATEGORIES, type=bool)
        QTreeWidgetItem.__init__(self)
        self.prod = prod
        if useCategories:
            icon = GeoAlgorithm.getDefaultIcon()
        self.setToolTip(0, prod)
        self.setText(0, prod)

