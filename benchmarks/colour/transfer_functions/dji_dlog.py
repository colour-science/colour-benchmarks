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

__all__ = ['DJI_DLOG_factories']

DJI_DLOG_factories = {
    'log_encoding_DJIDLog': colour.models.log_encoding_DJIDLog,
    'log_decoding_DJIDLog': colour.models.log_decoding_DJIDLog,
}

IJK_benchmark_factory(DJI_DLOG_factories, __name__)
