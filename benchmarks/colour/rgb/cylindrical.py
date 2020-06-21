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

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CYLINDRICAL_FACTORIES']


CYLINDRICAL_FACTORIES = {
    'RGB_to_HSL': colour.models.RGB_to_HSL,
    'RGB_to_HSV': colour.models.RGB_to_HSV,
    'HSL_to_RGB': colour.models.HSL_to_RGB,
    'HSV_to_RGB': colour.models.HSV_to_RGB,
}

RGB_benchmark_factory(CYLINDRICAL_FACTORIES, __name__)