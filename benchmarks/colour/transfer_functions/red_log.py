# -*- coding: utf-8 -*-
"""
"colour.models" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.ijk import IJK_benchmark_factory

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['RedLogFactories']

RedLogFactories = {
    'log_encoding_REDLog': colour.models.log_encoding_REDLog,
    'log_decoding_REDLog': colour.models.log_decoding_REDLog,
    'log_encoding_REDLogFilm': colour.models.log_encoding_REDLogFilm,
    'log_decoding_REDLogFilm': colour.models.log_decoding_REDLogFilm,
    'log_encoding_Log3G10': colour.models.log_encoding_Log3G10,
    'log_decoding_Log3G10': colour.models.log_decoding_Log3G10,
    'log_encoding_Log3G12': colour.models.log_encoding_Log3G12,
    'log_decoding_Log3G12': colour.models.log_decoding_Log3G12,
}

IJK_benchmark_factory(RedLogFactories, __name__)
