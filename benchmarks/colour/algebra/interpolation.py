# -*- coding: utf-8 -*-
"""
"colour.algebra" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import numpy as np
import os
from benchmarks.factories.RGB import IJK_SD,IJK_HD,IJK_UHD,LUT_TABLE

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'



__all__ = ['']

prng = np.random.RandomState(4)


class table_interpolation_trilinear():
    def time_sd(self):
        V_xyz = colour.algebra.random_triplet_generator(345600, random_state=prng)
        colour.algebra.table_interpolation_trilinear(V_xyz, LUT_TABLE)

    def time_hd(self):
        V_xyz = colour.algebra.random_triplet_generator(921600, random_state=prng)
        colour.algebra.table_interpolation_trilinear(V_xyz, LUT_TABLE)

    def time_uhd(self):
        V_xyz = colour.algebra.random_triplet_generator(2073600, random_state=prng)
        colour.algebra.table_interpolation_trilinear(V_xyz, LUT_TABLE)

class table_interpolation_tetrahedral():
    def time_sd(self):
        V_xyz = colour.algebra.random_triplet_generator(345600, random_state=prng)
        colour.algebra.table_interpolation_tetrahedral(V_xyz, LUT_TABLE)

    def time_hd(self):
        V_xyz = colour.algebra.random_triplet_generator(921600, random_state=prng)
        colour.algebra.table_interpolation_tetrahedral(V_xyz, LUT_TABLE)

    def time_uhd(self):
        V_xyz = colour.algebra.random_triplet_generator(2073600, random_state=prng)
        colour.algebra.table_interpolation_tetrahedral(V_xyz, LUT_TABLE)

class least_square_mapping_MoorePenrose():
    def time_sd(self):
        colour.algebra.least_square_mapping_MoorePenrose(IJK_SD, IJK_SD)
    #Fail
    def time_hd(self):
        colour.algebra.least_square_mapping_MoorePenrose(IJK_HD, IJK_HD)
    #Fail
    def time_uhd(self):
        colour.algebra.least_square_mapping_MoorePenrose(IJK_UHD, IJK_UHD)
