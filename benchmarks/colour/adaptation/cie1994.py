# -*- coding: utf-8 -*-
"""
"colour.adaptation" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import numpy as np
import os
from benchmarks.factories.RGB import RGB_benchmark_factory
from benchmarks.factories.RGB import IJK_SD,IJK_HD,IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CIE1994_FACTORIES']

test_arr = np.array([0.4476, 0.4074])

_CIE1994 = partial(
    colour.adaptation.chromatic_adaptation_CIE1994,
    xy_o1 = test_arr,
    xy_o2 = test_arr,
    Y_o = 20,
    E_o1 = 1000,
    E_o2 = 1000
    )

CIE1994_FACTORIES = {
    'chromatic_adaptation_CIE1994': _CIE1994,
}

RGB_benchmark_factory(CIE1994_FACTORIES, __name__)
