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

__all__ = ['SLOG_factories']

SLOG_factories = {
    'log_encoding_SLog': colour.models.log_encoding_SLog,
    'log_decoding_SLog': colour.models.log_decoding_SLog,
    'log_encoding_SLog2': colour.models.log_encoding_SLog2,
    'log_decoding_SLog2': colour.models.log_decoding_SLog2,
    'log_encoding_SLog3': colour.models.log_encoding_SLog3,
    'log_decoding_SLog3': colour.models.log_decoding_SLog3,
}

IJK_benchmark_factory(SLOG_factories, __name__)
