# -*- coding: utf-8 -*-
"""
"colour.algebra" sub-package Benchmarks
=======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.ijk import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = []


class NormaliseVector():
    def time_sd(self):
        colour.algebra.normalise_vector(IJK_SD)

    def time_hd(self):
        colour.algebra.normalise_vector(IJK_HD)

    def time_uhd(self):
        colour.algebra.normalise_vector(IJK_UHD)


class EuclideanDistance():
    def time_sd(self):
        colour.algebra.euclidean_distance(IJK_SD, IJK_SD)

    def time_hd(self):
        colour.algebra.euclidean_distance(IJK_HD, IJK_HD)

    def time_uhd(self):
        colour.algebra.euclidean_distance(IJK_UHD, IJK_UHD)
