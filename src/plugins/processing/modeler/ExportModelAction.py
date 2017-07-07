# -*- coding: utf-8 -*-

"""
***************************************************************************
    CreateNewModelAction.py
    ---------------------
    Date                 : April 2016
    Copyright            : (C) 2016 by DEIMOS Engenharia
    Email                : 
***************************************************************************
*                                                                         *
***************************************************************************
"""

__author__ = 'João Andrade'
__date__ = 'April 2016'
__copyright__ = '(C) 2016, DEIMOS Engenharia'

__revision__ = '$Format:%H$'

import os
from PyQt4 import QtGui
from processing.gui.ToolboxAction import ToolboxAction
from processing.modeler.ExportModelDialog import ExportModelDialog

class ExportModelAction(ToolboxAction):

    def __init__(self):
	self.name, self.i18n_name = self.trAction('Export model to TEP', 'ExportModelAction')
        self.group, self.i18n_group = self.trAction('Tools', 'ExportModelAction')

    def getIcon(self):
        return QtGui.QIcon(os.path.dirname(__file__) + '/../images/model.png')

    def execute(self):
        dlg = ExportModelDialog()
        dlg.exec_()
        if dlg.update:
            self.toolbox.updateProvider('model')
