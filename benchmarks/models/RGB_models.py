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

__all__ = ['RGB_FACTORIES']

IJK_SD_CMYK = colour.models.CMY_to_CMYK(IJK_SD)
IJK_HD_CMYK = colour.models.CMY_to_CMYK(IJK_HD)
IJK_UHD_CMYK = colour.models.CMY_to_CMYK(IJK_UHD)

_illuminant_XYZ = [0.34570, 0.35850]
_illuminant_RGB = [0.31270, 0.32900]
_RGB_to_RGB = partial(
    colour.models.RGB_to_RGB,
    input_colourspace=colour.models.ACES_2065_1_COLOURSPACE,
    output_colourspace=colour.models.sRGB_COLOURSPACE)

"""
_RGB_to_RGB_matrix = partial(
    colour.models.RGB_to_RGB_matrix,
    input_colourspace=colour.models.sRGB_COLOURSPACE,
    output_colourspace=colour.models.PROPHOTO_RGB_COLOURSPACE)
"""

_RGB_to_XYZ = partial(
    colour.models.RGB_to_XYZ,
    illuminant_RGB=_illuminant_RGB,
    illuminant_XYZ=_illuminant_XYZ,
    RGB_to_XYZ_matrix=colour.models.ADOBE_RGB_1998_COLOURSPACE.RGB_to_XYZ_matrix)

_XYZ_to_RGB = partial(
    colour.models.XYZ_to_RGB,
    illuminant_RGB=_illuminant_RGB,
    illuminant_XYZ=_illuminant_XYZ,
    XYZ_to_RGB_matrix = colour.models.ADOBE_RGB_1998_COLOURSPACE.XYZ_to_RGB_matrix)

_RGB_luminance = partial(
    colour.models.RGB_luminance,
    primaries=colour.models.ADOBE_RGB_1998_COLOURSPACE.primaries,
    whitepoint=colour.models.ADOBE_RGB_1998_COLOURSPACE.whitepoint)

RGB_FACTORIES = {
    'RGB_to_ICTCP':colour.models.RGB_to_ICTCP,
    'RGB_to_YCoCg':colour.models.RGB_to_YCoCg,
    'RGB_to_YcCbcCrc': colour.models.RGB_to_YcCbcCrc,
    'RGB_to_YCbCr': colour.models.RGB_to_YCbCr,
    'RGB_to_Prismatic': colour.models.RGB_to_Prismatic,
    'RGB_to_CMY': colour.models.RGB_to_CMY,
    'RGB_to_HSL': colour.models.RGB_to_HSL,
    'RGB_to_HSV': colour.models.RGB_to_HSV,
    'RGB_to_RGB': _RGB_to_RGB,
    'RGB_luminance': _RGB_luminance,
    'RGB_to_XYZ': _RGB_to_XYZ,
    'sRGB_to_XYZ': colour.models.sRGB_to_XYZ,
    'ICTCP_to_RGB': colour.models.ICTCP_to_RGB,
    'YCoCg_to_RGB': colour.models.YCoCg_to_RGB,
    'YcCbcCrc_to_RGB': colour.models.YcCbcCrc_to_RGB,
    'YCbCr_to_RGB': colour.models.YCbCr_to_RGB,
    'Prismatic_to_RGB': colour.models.Prismatic_to_RGB,
    'CMY_to_RGB': colour.models.CMY_to_RGB,
    'CMY_to_CMYK': colour.models.CMY_to_CMYK,
    'CMYK_to_CMY': [colour.models.CMYK_to_CMY,IJK_SD_CMYK,IJK_HD_CMYK,IJK_UHD_CMYK],
    'HSL_to_RGB': colour.models.HSL_to_RGB,
    'HSV_to_RGB': colour.models.HSV_to_RGB,
    'XYZ_to_sRGB': colour.models.XYZ_to_sRGB,
    'XYZ_to_RGB': _XYZ_to_RGB

}

RGB_benchmark_factory(RGB_FACTORIES, __name__)
