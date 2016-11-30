"""
***************************************************************************
   ShareWorkflowAction.py
***************************************************************************
"""

from processing.gui.ToolboxAction import ToolboxAction
from processing_workflow.WorkflowShareDialog import WorkflowShareDialog
import os
from PyQt4 import QtGui
from processing.core.Processing import Processing
# Class for an action to be added to the SEXTANTE toolbar
class ShareWorkflowAction(ToolboxAction):

    def __init__(self, workflowProvider):
		self.name="Share workflow"
		self.group="Tools"
		self.workflowProvider = workflowProvider

    def getIcon(self):
        return QtGui.QIcon(os.path.dirname(__file__) + "/images/icon.png")

    def execute(self):
        dlg = WorkflowShareDialog(self)
        dlg.exec_()
	try:
            if dlg.update:
                self.toolbox.updateProvider('workflow')
	except Exception:
	    pass
