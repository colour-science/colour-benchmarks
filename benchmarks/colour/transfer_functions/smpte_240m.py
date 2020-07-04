# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.ijk import IJK_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['SmpteFactories']

SmpteFactories = {
    'oetf_SMPTE240M': colour.models.oetf_SMPTE240M,
    'eotf_SMPTE240M': colour.models.eotf_SMPTE240M,
}

IJK_benchmark_factory(SmpteFactories, __name__)
