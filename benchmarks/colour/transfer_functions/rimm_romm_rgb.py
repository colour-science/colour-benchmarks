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

__all__ = ['RIMMROMM_FACTORIES']

RIMMROMM_FACTORIES = {
    'cctf_encoding_ROMMRGB': colour.models.cctf_encoding_ROMMRGB,
    'cctf_decoding_ROMMRGB': colour.models.cctf_decoding_ROMMRGB,
    'cctf_encoding_ProPhotoRGB': colour.models.cctf_encoding_ProPhotoRGB,
    'cctf_decoding_ProPhotoRGB': colour.models.cctf_decoding_ProPhotoRGB,
    'cctf_encoding_RIMMRGB': colour.models.cctf_encoding_RIMMRGB,
    'cctf_decoding_RIMMRGB': colour.models.cctf_decoding_RIMMRGB,
    'log_encoding_ERIMMRGB': colour.models.log_encoding_ERIMMRGB,
    'log_decoding_ERIMMRGB': colour.models.log_decoding_ERIMMRGB,
}

RGB_benchmark_factory(RIMMROMM_FACTORIES, __name__)
