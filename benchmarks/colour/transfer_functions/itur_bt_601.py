# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals
from functools import partial
import colour
import os
from benchmarks.factories.RGB import IJK_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['BT601_FACTORIES']

BT601_FACTORIES = {
    'oetf_BT601': colour.models.oetf_BT601,
    'oetf_inverse_BT601': colour.models.oetf_inverse_BT601,
}

IJK_benchmark_factory(BT601_FACTORIES, __name__)
