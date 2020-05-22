# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.RGB import RGB_benchmark_factory
__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['RGB_FACTORIES']

RGB_FACTORIES = {
    'RGB_to_ICTCP':colour.models.RGB_to_ICTCP,
    'RGB_to_YCoCg':colour.models.RGB_to_YCoCg,
    'RGB_to_YcCbcCrc': colour.models.RGB_to_YcCbcCrc,
    'RGB_to_YCbCr': colour.models.RGB_to_YCbCr,
    'RGB_to_Prismatic': colour.models.RGB_to_Prismatic,
    'RGB_to_CMY': colour.models.RGB_to_CMY,
    'RGB_to_HSL': colour.models.RGB_to_HSL,
    'RGB_to_HSV': colour.models.RGB_to_HSV
}

RGB_benchmark_factory(RGB_FACTORIES, __name__)
