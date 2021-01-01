# -*- coding: utf-8 -*-
"""
"colour.volume" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.ijk import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = []


class IsWithinVisibleSpectrum():
    timeout = 120.0

    def time_sd(self):
        colour.volume.is_within_visible_spectrum(IJK_SD)

    def time_hd(self):
        colour.volume.is_within_visible_spectrum(IJK_HD)

    def time_uhd(self):
        colour.volume.is_within_visible_spectrum(IJK_UHD)


class IsWithinPointerGamut():
    def time_sd(self):
        colour.volume.is_within_pointer_gamut(IJK_SD)

    def time_hd(self):
        colour.volume.is_within_pointer_gamut(IJK_HD)

    def time_uhd(self):
        colour.volume.is_within_pointer_gamut(IJK_UHD)


class IsWithinMacadamLimits():
    def time_sd(self):
        colour.volume.is_within_macadam_limits(IJK_SD, 'A')

    def time_hd(self):
        colour.volume.is_within_macadam_limits(IJK_HD, 'A')

    # Fail
    def time_uhd(self):
        colour.volume.is_within_macadam_limits(IJK_UHD, 'A')
