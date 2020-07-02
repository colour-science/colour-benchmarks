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

__all__ = ['KRYSTEK_FACTORIES']

IJK_SD_XY = IJK_SD[:,:,0:2]
IJK_HD_XY = IJK_HD[:,:,0:2]
IJK_UHD_XY = IJK_UHD[:,:,0:2]

IJK_SD_LIMITED = IJK_SD[0:50,0:50,0:2]
IJK_HD_LIMITED= IJK_HD[0:100,0:100,0:2]
IJK_UHD_LIMITED = IJK_UHD[0:200,0:200,0:2]


KRYSTEK_FACTORIES = {
    'CCT_to_uv_Krystek1985': [colour.temperature.CCT_to_uv_Krystek1985,
    IJK_SD_LIMITED, IJK_HD_LIMITED, IJK_UHD_LIMITED]

    'uv_to_CCT_Krystek1985': [colour.temperature.uv_to_CCT_Krystek1985,
                        IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY]
}

RGB_benchmark_factory(KRYSTEK_FACTORIES, __name__)
