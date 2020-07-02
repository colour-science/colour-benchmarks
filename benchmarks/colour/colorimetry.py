# -*- coding: utf-8 -*-
"""
"colour.colorimetry" sub-package Benchmarks
======================================
"""

from __future__ import division, unicode_literals

import colour

from benchmarks.factories.RGB import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['']


class yellowness_ASTME313():
    def time_sd(self):
        colour.colorimetry.yellowness_ASTME313(IJK_SD)

    def time_hd(self):
        colour.colorimetry.yellowness_ASTME313(IJK_HD)

    def time_uhd(self):
        colour.colorimetry.yellowness_ASTME313(IJK_UHD)


class whiteness_CIE2004():
    def time_sd(self):
        colour.colorimetry.whiteness_CIE2004(IJK_SD[:, :, 0:2], 20,
                                             IJK_SD[:, :, 0:2])

    def time_hd(self):
        colour.colorimetry.whiteness_CIE2004(IJK_HD[:, :, 0:2], 20,
                                             IJK_HD[:, :, 0:2])

    def time_uhd(self):
        colour.colorimetry.whiteness_CIE2004(IJK_UHD[:, :, 0:2], 20,
                                             IJK_UHD[:, :, 0:2])


class luminance_CIE1976():
    def time_sd(self):
        colour.colorimetry.luminance_CIE1976(IJK_SD)

    def time_hd(self):
        colour.colorimetry.luminance_CIE1976(IJK_HD)

    def time_uhd(self):
        colour.colorimetry.luminance_CIE1976(IJK_UHD)


class intermediate_luminance_function_CIE1976():
    def time_sd(self):
        colour.colorimetry.intermediate_luminance_function_CIE1976(IJK_SD)

    def time_hd(self):
        colour.colorimetry.intermediate_luminance_function_CIE1976(IJK_HD)

    def time_uhd(self):
        colour.colorimetry.intermediate_luminance_function_CIE1976(IJK_UHD)


class lightness_CIE1976():
    def time_sd(self):
        colour.colorimetry.lightness_CIE1976(IJK_SD)

    def time_hd(self):
        colour.colorimetry.lightness_CIE1976(IJK_HD)

    def time_uhd(self):
        colour.colorimetry.lightness_CIE1976(IJK_UHD)


class intermediate_lightness_function_CIE1976():
    def time_sd(self):
        colour.colorimetry.intermediate_lightness_function_CIE1976(IJK_SD)

    def time_hd(self):
        colour.colorimetry.intermediate_lightness_function_CIE1976(IJK_HD)

    def time_uhd(self):
        colour.colorimetry.intermediate_lightness_function_CIE1976(IJK_UHD)
