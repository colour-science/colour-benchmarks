# -*- coding: utf-8 -*-
"""
"colour.temperature" sub-package Benchmarks
===========================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.RGB import IJK_benchmark_factory
from benchmarks.factories.RGB import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['HERNANDEZ_FACTORIES']

IJK_SD_XY = IJK_SD[0:50, 0:50, 0:2]
IJK_HD_XY = IJK_HD[0:100, 0:100, 0:2]
IJK_UHD_XY = IJK_UHD[0:200, 0:200, 0:2]

HERNANDEZ_FACTORIES = {
    'CCT_to_xy_Hernandez1999': [
        colour.temperature.CCT_to_xy_Hernandez1999, IJK_SD_XY, IJK_HD_XY,
        IJK_UHD_XY
    ],
    'xy_to_CCT_Hernandez1999': [
        colour.temperature.xy_to_CCT_Hernandez1999, IJK_SD_XY, IJK_HD_XY,
        IJK_UHD_XY
    ]
}

IJK_benchmark_factory(HERNANDEZ_FACTORIES, __name__)
