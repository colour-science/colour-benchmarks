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

__all__ = ['hdr_ipt_factories']

hdr_ipt_factories = {
    'XYZ_to_hdr_IPT': colour.models.XYZ_to_hdr_IPT,
    'hdr_IPT_to_XYZ': colour.models.hdr_IPT_to_XYZ,
}

IJK_benchmark_factory(hdr_ipt_factories, __name__)
