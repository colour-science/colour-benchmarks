# -*- coding: utf-8 -*-
"""
"colour.difference" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.differences import DeltaE_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['DIN_FACTORIES']

DIN_FACTORIES = {'delta_E_DIN99': colour.difference.delta_E_DIN99}

DeltaE_benchmark_factory(DIN_FACTORIES, __name__)
