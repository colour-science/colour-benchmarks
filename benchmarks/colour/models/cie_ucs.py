# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.ijk import IJK_benchmark_factory
from benchmarks.factories.ijk import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CieUcsFactories']

IJK_SD_XY = colour.models.UCS_to_uv(IJK_SD)
IJK_HD_XY = colour.models.UCS_to_uv(IJK_HD)
IJK_UHD_XY = colour.models.UCS_to_uv(IJK_UHD)

CieUcsFactories = {
    'XYZ_to_UCS':
    colour.models.XYZ_to_UCS,
    'UCS_to_XYZ':
    colour.models.UCS_to_XYZ,
    'UCS_to_uv':
    colour.models.UCS_to_uv,
    'uv_to_UCS': [colour.models.uv_to_UCS, IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY],
    'UCS_uv_to_xy':
    [colour.models.UCS_uv_to_xy, IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY],
    'xy_to_UCS_uv':
    [colour.models.xy_to_UCS_uv, IJK_SD_XY, IJK_HD_XY, IJK_UHD_XY],
}

IJK_benchmark_factory(CieUcsFactories, __name__)
