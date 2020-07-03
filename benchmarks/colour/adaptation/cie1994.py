# -*- coding: utf-8 -*-
"""
"colour.adaptation" sub-package Benchmarks
==========================================
"""

from __future__ import division, unicode_literals

import colour
import numpy as np
from functools import partial

from benchmarks.factories.RGB import IJK_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CIE1994_factories']

test_arr = np.array([0.4476, 0.4074])

_CIE1994 = partial(
    colour.adaptation.chromatic_adaptation_CIE1994,
    xy_o1=test_arr,
    xy_o2=test_arr,
    Y_o=20,
    E_o1=1000,
    E_o2=1000)

CIE1994_factories = {
    'chromatic_adaptation_CIE1994': _CIE1994,
}

IJK_benchmark_factory(CIE1994_factories, __name__)
