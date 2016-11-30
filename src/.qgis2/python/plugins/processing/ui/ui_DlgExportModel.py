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

class ui_DlgExportModel(object):
    def setupUi(self, DlgExportModel):
        DlgExportModel.setObjectName(_fromUtf8("DlgExportModel"))
        DlgExportModel.setFixedSize(318, 250)
        self.verticalLayout = QtGui.QVBoxLayout(DlgExportModel)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setMargin(9)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setMargin(3)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.btnExport = QtGui.QToolButton(DlgExportModel)
        self.btnExport.setObjectName(_fromUtf8("btnExport"))

        self.horizontalLayout.addWidget(self.btnExport)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(DlgExportModel)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.tabWidget = QtGui.QTabWidget(self.splitter)
        self.tabWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.South)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.searchBox = QgsFilterLineEdit(self.tab_2)
        self.searchBox.setObjectName(_fromUtf8("searchBox"))

        self.verticalLayout_3.addWidget(self.searchBox)
        self.algorithmTree = QtGui.QTreeWidget(self.tab_2)
        self.algorithmTree.setAlternatingRowColors(True)
        self.algorithmTree.setObjectName(_fromUtf8("algorithmTree"))
        self.algorithmTree.headerItem().setText(0, _fromUtf8("1"))
        self.algorithmTree.header().setVisible(False)
        self.verticalLayout_3.addWidget(self.algorithmTree)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))


	self.tab_3 = QtGui.QWidget()
	self.tab_3.setObjectName(_fromUtf8("tab_3"))

	self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(DlgExportModel)
        QtCore.QMetaObject.connectSlotsByName(DlgExportModel)

    def retranslateUi(self, DlgExportModel):
        DlgExportModel.setWindowTitle(_translate("DlgExportModel", "Export Models", None))
        self.searchBox.setToolTip(_translate("DlgExportModel", "Enter algorithm name to filter list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("DlgExportModel", "Models", None))

from qgis.gui import QgsFilterLineEdit
