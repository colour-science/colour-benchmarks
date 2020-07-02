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

__all__ = ['ACEScc_FACTORIES']

ACEScc_FACTORIES = {
    'log_encoding_ACEScc': colour.models.log_encoding_ACEScc,
    'log_decoding_ACEScc': colour.models.log_decoding_ACEScc,
    'log_encoding_ACEScct': colour.models.log_encoding_ACEScct,
    'log_decoding_ACEScct': colour.models.log_decoding_ACEScct,
    'log_encoding_ACESproxy': colour.models.log_encoding_ACESproxy,
    'log_decoding_ACESproxy': colour.models.log_decoding_ACESproxy,
}

IJK_benchmark_factory(ACEScc_FACTORIES, __name__)
