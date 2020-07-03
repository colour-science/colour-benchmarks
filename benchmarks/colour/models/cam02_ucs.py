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

__all__ = ['cam02_ucs_factories']

cam02_ucs_factories = {
    'JMh_CAM16_to_CAM16LCD': colour.models.JMh_CAM16_to_CAM16LCD,
    'CAM16LCD_to_JMh_CAM16': colour.models.CAM16LCD_to_JMh_CAM16,
    'JMh_CAM16_to_CAM16SCD': colour.models.JMh_CAM16_to_CAM16SCD,
    'CAM16SCD_to_JMh_CAM16': colour.models.CAM16SCD_to_JMh_CAM16,
    'JMh_CAM16_to_CAM16UCS': colour.models.JMh_CAM16_to_CAM16UCS,
    'CAM16UCS_to_JMh_CAM16': colour.models.CAM16UCS_to_JMh_CAM16,
}

IJK_benchmark_factory(cam02_ucs_factories, __name__)
