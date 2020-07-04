# -*- coding: utf-8 -*-
"""
"colour.difference" sub-package Benchmarks
==========================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.delta_e import DeltaE_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['DeltaEFactories']

DeltaEFactories = {
    'delta_E_CIE1976': colour.difference.delta_E_CIE1976,
    'delta_E_CIE1994': colour.difference.delta_E_CIE1994,
    'delta_E_CIE2000': colour.difference.delta_E_CIE2000,
    'delta_E_CMC': colour.difference.delta_E_CMC,
}

DeltaE_benchmark_factory(DeltaEFactories, __name__)
