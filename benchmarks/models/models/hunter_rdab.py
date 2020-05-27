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

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['CIE_HUNTER_RDAB_FACTORIES']

CIE_HUNTER_RDAB_FACTORIES = {
    'XYZ_to_Hunter_Rdab': colour.models.XYZ_to_Hunter_Rdab,
    'Hunter_Rdab_to_XYZ': colour.models.Hunter_Rdab_to_XYZ,
}

RGB_benchmark_factory(CIE_HUNTER_RDAB_FACTORIES, __name__)
