# -*- coding: utf-8 -*-
"""
"colour.appearance" sub-package Benchmarks
==========================================
"""

from __future__ import division, unicode_literals

import colour
import numpy as np

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

specification = colour.appearance.CIECAM02_Specification(
    J=41.731207905126638, C=0.103355738709070, h=217.067959767393010)

__all__ = []

array = np.array([1, 2, 3])


class XYZ_to_CIECAM02():
    def time_sd(self):
        colour.appearance.XYZ_to_CIECAM02(array, array, 20, 20)


class CIECAM02_to_XYZ():
    def time_sd(self):
        colour.appearance.CIECAM02_to_XYZ(specification, array, 20, 20)
