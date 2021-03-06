# -*- coding: utf-8 -*-
"""
"colour.utilities" sub-package Benchmarks
=========================================
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

__all__ = ['CommonFactories']

CommonFactories = {
    'to_domain_1': colour.utilities.to_domain_1,
    'to_domain_10': colour.utilities.to_domain_10,
    'to_domain_100': colour.utilities.to_domain_1,
    'to_domain_degrees': colour.utilities.to_domain_degrees,
    'to_domain_int': colour.utilities.to_domain_int,
    'from_range_1': colour.utilities.from_range_1,
    'from_range_10': colour.utilities.from_range_10,
    'from_range_100': colour.utilities.from_range_100,
    'from_range_degrees': colour.utilities.from_range_degrees,
    'from_range_int': colour.utilities.from_range_int,
}

IJK_benchmark_factory(CommonFactories, __name__)
