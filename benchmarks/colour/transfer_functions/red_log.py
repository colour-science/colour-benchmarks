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

__all__ = ['REDLOG_FACTORIES']

REDLOG_FACTORIES = {
    'log_encoding_REDLog': colour.models.log_encoding_REDLog,
    'log_decoding_REDLog': colour.models.log_decoding_REDLog,
    'log_encoding_REDLogFilm': colour.models.log_encoding_REDLogFilm,
    'log_decoding_REDLogFilm': colour.models.log_decoding_REDLogFilm,
    'log_encoding_Log3G10': colour.models.log_encoding_Log3G10,
    'log_decoding_Log3G10': colour.models.log_decoding_Log3G10,
    'log_encoding_Log3G12': colour.models.log_encoding_Log3G12,
    'log_decoding_Log3G12': colour.models.log_decoding_Log3G12,
}

IJK_benchmark_factory(REDLOG_FACTORIES, __name__)
