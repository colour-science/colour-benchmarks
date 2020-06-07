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

__all__ = ['ALEXALOG_FACTORIES']

ALEXALOG_FACTORIES = {
    'log_encoding_ALEXALogC': colour.models.log_encoding_ALEXALogC,
    'log_decoding_ALEXALogC': colour.models.log_decoding_ALEXALogC,
}

RGB_benchmark_factory(ALEXALOG_FACTORIES, __name__)
