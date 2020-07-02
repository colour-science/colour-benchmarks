# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import os
from benchmarks.factories.RGB import RGB_benchmark_factory
from benchmarks.factories.RGB import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CIE_XYY_FACTORIES']

IJK_SD_XY = colour.models.XYZ_to_xy(IJK_SD)
IJK_HD_XY = colour.models.XYZ_to_xy(IJK_HD)
IJK_UHD_XY = colour.models.XYZ_to_xy(IJK_UHD)

CIE_XYY_FACTORIES = {
    'XYZ_to_xyY': colour.models.XYZ_to_xyY,
    'xyY_to_XYZ': colour.models.xyY_to_XYZ,
    'xyY_to_xy': colour.models.xyY_to_xy,
    'XYZ_to_xy': colour.models.XYZ_to_xy,
    'xy_to_XYZ': [colour.models.xy_to_XYZ, IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY],
    'xy_to_xyY': [colour.models.xy_to_xyY, IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY],
}

RGB_benchmark_factory(CIE_XYY_FACTORIES, __name__)
