# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.RGB import IJK_benchmark_factory
from benchmarks.factories.RGB import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CMY_factories']

IJK_SD_CMYK = colour.models.CMY_to_CMYK(IJK_SD)
IJK_HD_CMYK = colour.models.CMY_to_CMYK(IJK_HD)
IJK_UHD_CMYK = colour.models.CMY_to_CMYK(IJK_UHD)

CMY_factories = {
    'RGB_to_CMY':
    colour.models.RGB_to_CMY,
    'CMY_to_RGB':
    colour.models.CMY_to_RGB,
    'CMY_to_CMYK':
    colour.models.CMY_to_CMYK,
    'CMYK_to_CMY':
    [colour.models.CMYK_to_CMY, IJK_SD_CMYK, IJK_HD_CMYK, IJK_UHD_CMYK],
}

IJK_benchmark_factory(CMY_factories, __name__)
