# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import os
from benchmarks.factories.RGB import IJK_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['COLOURSPACE_FACTORIES']

_illuminant_XYZ = [0.34570, 0.35850]
_illuminant_RGB = [0.31270, 0.32900]
_RGB_to_RGB = partial(
    colour.models.RGB_to_RGB,
    input_colourspace=colour.models.ACES_2065_1_COLOURSPACE,
    output_colourspace=colour.models.sRGB_COLOURSPACE)

_RGB_to_XYZ = partial(
    colour.models.RGB_to_XYZ,
    illuminant_RGB=_illuminant_RGB,
    illuminant_XYZ=_illuminant_XYZ,
    RGB_to_XYZ_matrix=colour.models.ADOBE_RGB_1998_COLOURSPACE.
    RGB_to_XYZ_matrix)

_XYZ_to_RGB = partial(
    colour.models.XYZ_to_RGB,
    illuminant_RGB=_illuminant_RGB,
    illuminant_XYZ=_illuminant_XYZ,
    XYZ_to_RGB_matrix=colour.models.ADOBE_RGB_1998_COLOURSPACE.
    XYZ_to_RGB_matrix)

_RGB_luminance = partial(
    colour.models.RGB_luminance,
    primaries=colour.models.ADOBE_RGB_1998_COLOURSPACE.primaries,
    whitepoint=colour.models.ADOBE_RGB_1998_COLOURSPACE.whitepoint)

COLOURSPACE_FACTORIES = {
    'RGB_to_RGB': _RGB_to_RGB,
    'RGB_luminance': _RGB_luminance,
    'RGB_to_XYZ': _RGB_to_XYZ,
    'XYZ_to_RGB': _XYZ_to_RGB
}

IJK_benchmark_factory(COLOURSPACE_FACTORIES, __name__)


class RGB_to_RGB_matrix():
    def time_func(self):
        colour.models.RGB_to_RGB_matrix(
            input_colourspace=colour.models.sRGB_COLOURSPACE,
            output_colourspace=colour.models.PROPHOTO_RGB_COLOURSPACE)
