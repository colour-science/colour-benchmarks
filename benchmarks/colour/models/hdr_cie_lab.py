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

__all__ = ['CIE_DIR_FACTORIES']

CIE_DIR_FACTORIES = {
    'XYZ_to_hdr_CIELab': colour.models.XYZ_to_hdr_CIELab,
    'hdr_CIELab_to_XYZ': colour.models.hdr_CIELab_to_XYZ,
}

IJK_benchmark_factory(CIE_DIR_FACTORIES, __name__)
