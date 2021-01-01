# -*- coding: utf-8 -*-
"""
"colour.utilities" sub-package Benchmarks
=========================================
"""

from __future__ import division, unicode_literals

import colour
import numpy as np
from functools import partial

from benchmarks.factories.ijk import IJK_benchmark_factory
from benchmarks.factories.ijk import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['ArrayFactories']

_dot_vector = partial(
    colour.utilities.dot_vector,
    v=np.array([0.20654008, 0.12197225, 0.05136952]))

_linear_conversion = partial(
    colour.utilities.linear_conversion,
    old_range=np.array([0, 360]),
    new_range=np.array([0, 1]))

ArrayFactories = {
    'as_array': colour.utilities.as_array,
    'as_int_array': colour.utilities.as_int_array,
    'as_float_array': colour.utilities.as_float_array,
    'as_numeric': colour.utilities.as_numeric,
    'as_int': colour.utilities.as_int,
    'as_float': colour.utilities.as_float,
    'normalise_maximum': colour.utilities.normalise_maximum,
    'tstack': colour.utilities.tstack,
    'tsplit': colour.utilities.tsplit,
    'row_as_diagonal': colour.utilities.row_as_diagonal,
    'dot_vector': _dot_vector,
    'linear_conversion': _linear_conversion,
}

IJK_benchmark_factory(ArrayFactories, __name__)


class dot_matrix():
    def time_sd(self):
        colour.utilities.dot_matrix(
            IJK_SD[0:3, 0:3, 0:3], IJK_SD[0:3, 0:3, 0:3])

    def time_hd(self):
        colour.utilities.dot_matrix(
            IJK_HD[0:3, 0:3, 0:3], IJK_HD[0:3, 0:3, 0:3])

    def time_uhd(self):
        colour.utilities.dot_matrix(
            IJK_UHD[0:3, 0:3, 0:3], IJK_UHD[0:3, 0:3, 0:3])


class lerp():
    def time_sd(self):
        colour.utilities.lerp(IJK_SD, IJK_SD, IJK_SD)

    def time_hd(self):
        colour.utilities.lerp(IJK_HD, IJK_HD, IJK_HD)

    def time_uhd(self):
        colour.utilities.lerp(IJK_UHD, IJK_UHD, IJK_UHD)
