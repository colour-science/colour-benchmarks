# -*- coding: utf-8 -*-
"""
"colour.notation" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.RGB import IJK_benchmark_factory
from benchmarks.factories.RGB import IJK_SD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['NOTATION_FACTORIES']

RGB = [0.6667, 0.45, 0.8]
HEX = colour.notation.RGB_to_HEX(RGB)

NOTATION_FACTORIES = {
    'munsell_value_Priest1920': colour.notation.munsell_value_Priest1920,
    'munsell_value_Munsell1933': colour.notation.munsell_value_Munsell1933,
    'munsell_value_Moon1943': colour.notation.munsell_value_Moon1943,
    'munsell_value_Saunderson1944':
    colour.notation.munsell_value_Saunderson1944,
    'munsell_value_Ladd1955': colour.notation.munsell_value_Ladd1955,
    'munsell_value_McCamy1987': colour.notation.munsell_value_McCamy1987,
    'munsell_value_ASTMD1535': colour.notation.munsell_value_ASTMD1535,
}


class xyY_to_munsell_colour():
    def time_func(self):
        colour.notation.xyY_to_munsell_colour(IJK_SD[0:10, 0:10, :])


class RGB_to_HEX():
    def time_func(self):
        colour.notation.RGB_to_HEX(RGB)


class HEX_to_RGB():
    def time_func(self):
        colour.notation.HEX_to_RGB(HEX)


IJK_benchmark_factory(NOTATION_FACTORIES, __name__)
