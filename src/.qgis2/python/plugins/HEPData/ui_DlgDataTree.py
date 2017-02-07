# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class ui_DlgDataTree(object):
    def setupUi(self, DlgDataTree):
        DlgDataTree.setObjectName(_fromUtf8("DlgDataTree"))
        DlgDataTree.resize(300, 300)
        self.verticalLayout = QtGui.QVBoxLayout(DlgDataTree)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setMargin(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.btnDownload = QtGui.QToolButton(DlgDataTree)
        self.btnDownload.setObjectName(_fromUtf8("btnDownload"))

	self.btnConfig = QtGui.QToolButton(DlgDataTree)
	self.btnConfig.setObjectName(_fromUtf8("btnConfig"))

        self.horizontalLayout.addWidget(self.btnDownload)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(DlgDataTree)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
	self.horizontalLayout.addWidget(self.btnConfig)
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.searchBox = QgsFilterLineEdit(self.tab_2)
        self.searchBox.setObjectName(_fromUtf8("searchBox"))

        self.verticalLayout_3.addWidget(self.searchBox)
        self.dataTree = QtGui.QTreeWidget(self.tab_2)
        self.dataTree.setAlternatingRowColors(True)
        self.dataTree.setObjectName(_fromUtf8("dataTree"))
        self.dataTree.headerItem().setText(0, _fromUtf8("1"))
        self.dataTree.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.dataTree)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

	self.verticalLayout.addWidget(self.splitter)

	self.progressBar = QtGui.QProgressBar(DlgDataTree)
	self.verticalLayout.addWidget(self.progressBar)

        self.retranslateUi(DlgDataTree)
        QtCore.QMetaObject.connectSlotsByName(DlgDataTree)

    def retranslateUi(self, DlgDataTree):
        DlgDataTree.setWindowTitle(_translate("DlgDataTree", "HEP Data Packages", None))
        self.searchBox.setToolTip(_translate("DlgDataTree", "Search Data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DlgDataTree", "Data", None))

from qgis.gui import QgsFilterLineEdit
