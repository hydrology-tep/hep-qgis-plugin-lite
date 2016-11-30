"""
***************************************************************************
    ProcessingGpfPlugin.py
-------------------------------------
    Copyright (C) 2014 TIGER-NET (www.tiger-net.org)

***************************************************************************
* This plugin is part of the Water Observation Information System (WOIS)  *
* developed under the TIGER-NET project funded by the European Space      *
* Agency as part of the long-term TIGER initiative aiming at promoting    *
* the use of Earth Observation (EO) for improved Integrated Water         *
* Resources Management (IWRM) in Africa.                                  *
*                                                                         *
* WOIS is a free software i.e. you can redistribute it and/or modify      *
* it under the terms of the GNU General Public License as published       *
* by the Free Software Foundation, either version 3 of the License,       *
* or (at your option) any later version.                                  *
*                                                                         *
* WOIS is distributed in the hope that it will be useful, but WITHOUT ANY * 
* WARRANTY; without even the implied warranty of MERCHANTABILITY or       *
* FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License   *
* for more details.                                                       *
*                                                                         *
* You should have received a copy of the GNU General Public License along *
* with this program.  If not, see <http://www.gnu.org/licenses/>.         *
***************************************************************************
"""

from qgis.core import *
import os, sys
import inspect
from processing.core.Processing import Processing
from processing_gpf.BEAMAlgorithmProvider import BEAMAlgorithmProvider 
from processing_gpf.S1TbxAlgorithmProvider import S1TbxAlgorithmProvider 

cmd_folder = os.path.split(inspect.getfile( inspect.currentframe() ))[0]
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

class ProcessingGpfPlugin:

    def __init__(self, iface):
        self.BeamProvider = BEAMAlgorithmProvider()
        self.S1TbxProvider = S1TbxAlgorithmProvider()
        self.iface = iface
        
    def initGui(self):
        Processing.addProvider(self.BeamProvider, True)
        Processing.addProvider(self.S1TbxProvider, True)

    def unload(self):
        Processing.removeProvider(self.BeamProvider)
        Processing.removeProvider(self.S1TbxProvider)
