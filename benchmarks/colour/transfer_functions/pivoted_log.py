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

__all__ = ['PIVOTEDLOG_FACTORIES']

PIVOTEDLOG_FACTORIES = {
    'log_encoding_PivotedLog': colour.models.log_encoding_PivotedLog,
    'log_decoding_PivotedLog': colour.models.log_decoding_PivotedLog,
}

RGB_benchmark_factory(PIVOTEDLOG_FACTORIES, __name__)