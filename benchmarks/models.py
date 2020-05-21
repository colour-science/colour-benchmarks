# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.common import triplet_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['COLOUR_MODELS_FACTORIES']

COLOUR_MODELS_FACTORIES = {
    'XYZ_to_xyY': colour.models.XYZ_to_xyY,
    'xyY_to_XYZ': colour.models.xyY_to_XYZ,
    'xyY_to_xy': colour.models.xyY_to_xy,
    'xy_to_xyY': colour.models.xy_to_xyY,
    'XYZ_to_xy': colour.models.XYZ_to_xy,
    'xy_to_XYZ': colour.models.xy_to_XYZ,
    'XYZ_to_Lab': colour.models.XYZ_to_Lab,
    'Lab_to_XYZ': colour.models.Lab_to_XYZ,
    'Lab_to_LCHab': colour.models.Lab_to_LCHab,
    'LCHab_to_Lab': colour.models.LCHab_to_Lab,
}

triplet_benchmark_factory(COLOUR_MODELS_FACTORIES, __name__)
