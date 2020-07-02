# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.RGB import IJK_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['ST2084_FACTORIES']

ST2084_FACTORIES = {
    'eotf_ST2084': colour.models.eotf_ST2084,
    'eotf_inverse_ST2084': colour.models.eotf_inverse_ST2084,
}

IJK_benchmark_factory(ST2084_FACTORIES, __name__)
