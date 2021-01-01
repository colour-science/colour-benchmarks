# -*- coding: utf-8 -*-
"""
"colour.algebra" sub-package Benchmarks
=======================================
"""

from __future__ import division, unicode_literals

import colour
import numpy as np

from benchmarks.factories.ijk import IJK_SD, IJK_HD, IJK_UHD, LUT_TABLE

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = []

prng = np.random.RandomState(4)


class TableInterpolationTrilinear():
    def time_sd(self):
        V_xyz = colour.algebra.random_triplet_generator(
            345600, random_state=prng)
        colour.algebra.table_interpolation_trilinear(V_xyz, LUT_TABLE)

    def time_hd(self):
        V_xyz = colour.algebra.random_triplet_generator(
            921600, random_state=prng)
        colour.algebra.table_interpolation_trilinear(V_xyz, LUT_TABLE)

    def time_uhd(self):
        V_xyz = colour.algebra.random_triplet_generator(
            2073600, random_state=prng)
        colour.algebra.table_interpolation_trilinear(V_xyz, LUT_TABLE)


class TableInterpolationTetrahedral():
    def time_sd(self):
        V_xyz = colour.algebra.random_triplet_generator(
            345600, random_state=prng)
        colour.algebra.table_interpolation_tetrahedral(V_xyz, LUT_TABLE)

    def time_hd(self):
        V_xyz = colour.algebra.random_triplet_generator(
            921600, random_state=prng)
        colour.algebra.table_interpolation_tetrahedral(V_xyz, LUT_TABLE)

    def time_uhd(self):
        V_xyz = colour.algebra.random_triplet_generator(
            2073600, random_state=prng)
        colour.algebra.table_interpolation_tetrahedral(V_xyz, LUT_TABLE)


class LeastSquareMappingMoorePenrose():
    def time_sd(self):
        colour.algebra.least_square_mapping_MoorePenrose(IJK_SD, IJK_SD)

    # Fail
    def time_hd(self):
        colour.algebra.least_square_mapping_MoorePenrose(IJK_HD, IJK_HD)

    # Fail
    def time_uhd(self):
        colour.algebra.least_square_mapping_MoorePenrose(IJK_UHD, IJK_UHD)
