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

__all__ = ['CieDinFactories']

CieDinFactories = {
    'Lab_to_DIN99': colour.models.Lab_to_DIN99,
    'DIN99_to_Lab': colour.models.DIN99_to_Lab,
}

IJK_benchmark_factory(CieDinFactories, __name__)
