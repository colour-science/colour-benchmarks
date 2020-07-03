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

__all__ = ['DCDM_factories']

DCDM_factories = {
    'eotf_DCDM': colour.models.eotf_DCDM,
    'eotf_inverse_DCDM': colour.models.eotf_inverse_DCDM,
}

IJK_benchmark_factory(DCDM_factories, __name__)
