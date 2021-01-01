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

__all__ = ['IptFactories']

IptFactories = {
    'XYZ_to_IPT': colour.models.XYZ_to_IPT,
    'IPT_to_XYZ': colour.models.IPT_to_XYZ,
    'IPT_hue_angle': colour.models.IPT_hue_angle,
}

IJK_benchmark_factory(IptFactories, __name__)
