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

__all__ = ['FILMLIGHT_TLOG_factories']

FILMLIGHT_TLOG_factories = {
    'log_encoding_FilmLightTLog': colour.models.log_encoding_FilmLightTLog,
    'log_decoding_FilmLightTLog': colour.models.log_decoding_FilmLightTLog,
}

IJK_benchmark_factory(FILMLIGHT_TLOG_factories, __name__)
