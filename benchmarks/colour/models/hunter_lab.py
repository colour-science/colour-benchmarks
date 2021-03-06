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

__all__ = ['HunterLabFactories']

HunterLabFactories = {
    'XYZ_to_Hunter_Lab': colour.models.XYZ_to_Hunter_Lab,
    'Hunter_Lab_to_XYZ': colour.models.Hunter_Lab_to_XYZ,
    'XYZ_to_K_ab_HunterLab1966': colour.models.XYZ_to_K_ab_HunterLab1966,
}

IJK_benchmark_factory(HunterLabFactories, __name__)
