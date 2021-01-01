# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.ijk import IJK_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CylindricalFactories']

CylindricalFactories = {
    'RGB_to_HSL': colour.models.RGB_to_HSL,
    'RGB_to_HSV': colour.models.RGB_to_HSV,
    'HSL_to_RGB': colour.models.HSL_to_RGB,
    'HSV_to_RGB': colour.models.HSV_to_RGB,
}

IJK_benchmark_factory(CylindricalFactories, __name__)
