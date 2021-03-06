# -*- coding: utf-8 -*-
"""
"colour.difference" sub-package Benchmarks
==========================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.delta_e import DeltaE_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['DeltaECam02Factories']

DeltaECam02Factories = {
    'delta_E_CAM02SCD': colour.difference.delta_E_CAM02SCD,
    'delta_E_CAM02LCD': colour.difference.delta_E_CAM02LCD,
    'delta_E_CAM02UCS': colour.difference.delta_E_CAM02UCS,
}

DeltaE_benchmark_factory(DeltaECam02Factories, __name__)
