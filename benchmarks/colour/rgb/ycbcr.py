# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.ijk import IJK_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['YcbcrFactories']

YcbcrFactories = {
    'RGB_to_YcCbcCrc': colour.models.RGB_to_YcCbcCrc,
    'RGB_to_YCbCr': colour.models.RGB_to_YCbCr,
    'YcCbcCrc_to_RGB': colour.models.YcCbcCrc_to_RGB,
    'YCbCr_to_RGB': colour.models.YCbCr_to_RGB,
}

IJK_benchmark_factory(YcbcrFactories, __name__)
