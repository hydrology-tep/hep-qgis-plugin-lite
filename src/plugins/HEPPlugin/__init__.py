# -*- coding: utf-8 -*-
"""
/***************************************************************************
 HEPData
                                 A QGIS plugin
 This plugin allows to get Data from HEP
                             -------------------
        begin                : 2016-05-23
        copyright            : (C) 2016 by DEIMOS Engenharia
        email                : joao.andrade@deimos.com.pt
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load HEPData class from file HEPData.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .hep_gen import HEPGen
    return HEPGen(iface)
