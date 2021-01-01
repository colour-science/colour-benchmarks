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

__all__ = ['DeltaECam16Factories']

DeltaECam16Factories = {
    'delta_E_CAM16LCD': colour.difference.delta_E_CAM16LCD,
    'delta_E_CAM16SCD': colour.difference.delta_E_CAM16SCD,
    'delta_E_CAM16UCS': colour.difference.delta_E_CAM16UCS,
}

DeltaE_benchmark_factory(DeltaECam16Factories, __name__)
