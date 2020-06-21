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
from benchmarks.factories.RGB import IJK_SD,IJK_HD,IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CIE_LUV_FACTORIES']

IJK_SD_XY = colour.models.Luv_to_uv(IJK_SD)
IJK_HD_XY = colour.models.Luv_to_uv(IJK_HD)
IJK_UHD_XY = colour.models.Luv_to_uv(IJK_UHD)

CIE_LUV_FACTORIES = {
    'XYZ_to_Luv': colour.models.XYZ_to_Luv,
    'Luv_to_XYZ': colour.models.Luv_to_XYZ,
    'Luv_to_uv': colour.models.Luv_to_uv,
    'Luv_to_LCHuv': colour.models.Luv_to_LCHuv,
    'LCHuv_to_Luv': colour.models.LCHuv_to_Luv,
    'Luv_uv_to_xy': [colour.models.Luv_uv_to_xy,IJK_SD_XY,
                  IJK_HD_XY,IJK_UHD_XY],
    'xy_to_Luv_uv': [colour.models.xy_to_Luv_uv,IJK_SD_XY,
                  IJK_HD_XY,IJK_UHD_XY],
    'uv_to_Luv': [colour.models.uv_to_Luv,IJK_SD_XY,
                  IJK_HD_XY,IJK_UHD_XY],
}

RGB_benchmark_factory(CIE_LUV_FACTORIES, __name__)
