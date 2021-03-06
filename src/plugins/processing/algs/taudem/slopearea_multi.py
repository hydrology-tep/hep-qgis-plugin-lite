# -*- coding: utf-8 -*-

"""
***************************************************************************
    slopearea_multi.py
    ---------------------
    Date                 : March 2015
    Copyright            : (C) 2015 by Alexander Bruy
    Email                : alexander dot bruy at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Alexander Bruy'
__date__ = 'March 2015'
__copyright__ = '(C) 2015, Alexander Bruy'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import os

from qgis.PyQt.QtGui import QIcon

from processing.core.GeoAlgorithm import GeoAlgorithm
from processing.core.ProcessingConfig import ProcessingConfig
from processing.core.GeoAlgorithmExecutionException import \
    GeoAlgorithmExecutionException

from processing.core.parameters import ParameterFile
from processing.core.parameters import ParameterNumber
from processing.core.outputs import OutputDirectory

from .TauDEMUtils import TauDEMUtils


class SlopeAreaMulti(GeoAlgorithm):

    SLOPE_GRID = 'SLOPE_GRID'
    AREA_GRID = 'AREA_GRID'
    SLOPE_EXPONENT = 'SLOPE_EXPONENT'
    AREA_EXPONENT = 'AREA_EXPONENT'

    SLOPE_AREA_GRID = 'SLOPE_AREA_GRID'

    def getIcon(self):
        return QIcon(os.path.dirname(__file__) + '/../../images/taudem.svg')

    def defineCharacteristics(self):
        self.name, self.i18n_name = self.trAlgorithm('Slope Area Combination (multifile)')
        self.cmdName = 'slopearea'
        self.group, self.i18n_group = self.trAlgorithm('Stream Network Analysis tools')

        self.addParameter(ParameterFile(self.SLOPE_GRID,
                                        self.tr('Slope Grid'), True, False))
        self.addParameter(ParameterFile(self.AREA_GRID,
                                        self.tr('Contributing Area Grid'), True, False))
        self.addParameter(ParameterNumber(self.SLOPE_EXPONENT,
                                          self.tr('Slope Exponent'), 0, None, 2))
        self.addParameter(ParameterNumber(self.AREA_EXPONENT,
                                          self.tr('Area Exponent'), 0, None, 1))

        self.addOutput(OutputDirectory(self.SLOPE_AREA_GRID,
                                       self.tr('Slope Area Grid')))

    def processAlgorithm(self, progress):
        commands = []
        commands.append(os.path.join(TauDEMUtils.mpiexecPath(), 'mpiexec'))

        processNum = ProcessingConfig.getSetting(TauDEMUtils.MPI_PROCESSES)
        if processNum <= 0:
            raise GeoAlgorithmExecutionException(
                self.tr('Wrong number of MPI processes used. Please set '
                        'correct number before running TauDEM algorithms.'))

        commands.append('-n')
        commands.append(unicode(processNum))
        commands.append(os.path.join(TauDEMUtils.taudemMultifilePath(), self.cmdName))
        commands.append('-slp')
        commands.append(self.getParameterValue(self.SLOPE_GRID))
        commands.append('-sca')
        commands.append(self.getParameterValue(self.AREA_GRID))
        commands.append('-par')
        commands.append(unicode(self.getParameterValue(self.SLOPE_EXPONENT)))
        commands.append(unicode(self.getParameterValue(self.AREA_EXPONENT)))
        commands.append('-sa')
        commands.append(self.getOutputValue(self.SLOPE_AREA_GRID))

        TauDEMUtils.executeTauDEM(commands, progress)
