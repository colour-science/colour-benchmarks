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

__all__ = ['BT2100_FACTORIES']

BT2100_FACTORIES = {
    'oetf_PQ_BT2100': colour.models.oetf_PQ_BT2100,
    'oetf_inverse_PQ_BT2100': colour.models.oetf_inverse_PQ_BT2100,
    'eotf_PQ_BT2100': colour.models.eotf_PQ_BT2100,
    'eotf_inverse_PQ_BT2100': colour.models.eotf_inverse_PQ_BT2100,
    'ootf_PQ_BT2100': colour.models.ootf_PQ_BT2100,
    'ootf_inverse_PQ_BT2100': colour.models.ootf_inverse_PQ_BT2100,
    'oetf_HLG_BT2100': colour.models.oetf_HLG_BT2100,
    'oetf_inverse_HLG_BT2100': colour.models.oetf_inverse_HLG_BT2100,
    'eotf_HLG_BT2100': colour.models.eotf_HLG_BT2100,
    'eotf_inverse_HLG_BT2100': colour.models.eotf_inverse_HLG_BT2100,
    'ootf_HLG_BT2100': colour.models.ootf_HLG_BT2100,
    'ootf_inverse_HLG_BT2100': colour.models.ootf_inverse_HLG_BT2100,
}

IJK_benchmark_factory(BT2100_FACTORIES, __name__)
