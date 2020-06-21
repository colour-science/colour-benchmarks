# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import os
from benchmarks.factories.RGB import RGB_benchmark_factory
from benchmarks.factories.RGB import IJK_SD,IJK_HD,IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CIE_OSA_UCS_FACTORIES']

CIE_OSA_UCS_FACTORIES = {
    'XYZ_to_OSA_UCS': colour.models.XYZ_to_OSA_UCS,
    # 'OSA_UCS_to_XYZ': colour.models.OSA_UCS_to_XYZ,
}

RGB_benchmark_factory(CIE_OSA_UCS_FACTORIES, __name__)
