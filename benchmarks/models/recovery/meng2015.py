# -*- coding: utf-8 -*-
"""
"colour.recovery" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import os
import numpy as np
from benchmarks.factories.RGB import RGB_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['MENG']

class MENG():

    def time_func(self):
        colour.recovery.XYZ_to_sd_Meng2015(np.array([1,2,2]))