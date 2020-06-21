# -*- coding: utf-8 -*-
"""
"colour.temprature" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import os
import numpy as np
from benchmarks.factories.RGB import RGB_benchmark_factory
from benchmarks.factories.RGB import IJK_SD,IJK_HD,IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['KANG_FACTORIES']

IJK_SD_XY = IJK_SD[0:50,0:50,0:2]
IJK_HD_XY = IJK_HD[0:100,0:100,0:2]
IJK_UHD_XY = IJK_UHD[0:200,0:200,0:2]

KANG_FACTORIES = {
    'CCT_to_xy_Kang2002': colour.temperature.CCT_to_xy_Kang2002,
    'xy_to_CCT_Kang2002': [colour.temperature.xy_to_CCT_Kang2002,
                        IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY]
}

RGB_benchmark_factory(KANG_FACTORIES, __name__)

