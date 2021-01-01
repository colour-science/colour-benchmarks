# -*- coding: utf-8 -*-
"""
"colour.temprature" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.RGB import IJK_benchmark_factory
from benchmarks.factories.RGB import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['OHNO_FACTORIES']

IJK_SD_XY = IJK_SD[:, :, 0:2]
IJK_HD_XY = IJK_HD[:, :, 0:2]
IJK_UHD_XY = IJK_UHD[:, :, 0:2]

OHNO_FACTORIES = {
    'CCT_to_uv_Ohno2013':
    colour.temperature.CCT_to_uv_Ohno2013,
    'uv_to_CCT_Ohno2013':
    [colour.temperature.uv_to_CCT_Ohno2013, IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY]
}

IJK_benchmark_factory(OHNO_FACTORIES, __name__)
