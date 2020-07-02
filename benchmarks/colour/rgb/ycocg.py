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

__all__ = ['YCOCG_FACTORIES']

YCOCG_FACTORIES = {
    'RGB_to_YCoCg': colour.models.RGB_to_YCoCg,
    'YCoCg_to_RGB': colour.models.YCoCg_to_RGB,
}

IJK_benchmark_factory(YCOCG_FACTORIES, __name__)
