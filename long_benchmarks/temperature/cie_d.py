# -*- coding: utf-8 -*-
"""
"colour.temprature" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.RGB import IJK_benchmark_factory
from benchmarks.factories.RGB import IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CIE_FACTORIES']

IJK_SD_XY = IJK_UHD[0:100, 0:100, 0:2]
IJK_HD_XY = IJK_UHD[0:300, 0:300, 0:2]
IJK_UHD_XY = IJK_UHD[0:512, 0:512, 0:2]

CIE_FACTORIES = {
    'CCT_to_xy_CIE_D':
    colour.temperature.CCT_to_xy_CIE_D,
    'xy_to_CCT_CIE_D':
    [colour.temperature.xy_to_CCT_CIE_D, IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY]
}

IJK_benchmark_factory(CIE_FACTORIES, __name__)
