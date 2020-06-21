# -*- coding: utf-8 -*-
"""
"colour.difference" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import os
import numpy as np
from benchmarks.factories.differences import DIFFERENCES_benchmark_factory
from colour.models.cam02_ucs import COEFFICIENTS_UCS_LUO2006

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CAM02_FACTORIES']


CAM02_FACTORIES = {
    'delta_E_CAM02SCD': colour.difference.delta_E_CAM02SCD,
    'delta_E_CAM02LCD': colour.difference.delta_E_CAM02LCD,
    'delta_E_CAM02UCS': colour.difference.delta_E_CAM02UCS,
}

DIFFERENCES_benchmark_factory(CAM02_FACTORIES, __name__)

