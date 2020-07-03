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

__all__ = ['ARIB_factories']

ARIB_factories = {
    'oetf_ARIBSTDB67': colour.models.oetf_ARIBSTDB67,
    'oetf_inverse_ARIBSTDB67': colour.models.oetf_inverse_ARIBSTDB67,
}

IJK_benchmark_factory(ARIB_factories, __name__)
