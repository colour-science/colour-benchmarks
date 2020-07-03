# -*- coding: utf-8 -*-
"""
"colour.adaptations" sub-package Benchmarks
===========================================
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


class chromatic_adaptation_forward_CMCCAT2000():
    def time_sd(self):
        colour.adaptation.chromatic_adaptation_forward_CMCCAT2000(
            IJK_SD, IJK_SD, IJK_SD, 200, 200)

    def time_hd(self):
        colour.adaptation.chromatic_adaptation_forward_CMCCAT2000(
            IJK_HD, IJK_HD, IJK_HD, 200, 200)

    def time_uhd(self):
        colour.adaptation.chromatic_adaptation_forward_CMCCAT2000(
            IJK_UHD, IJK_UHD, IJK_UHD, 200, 200)


class chromatic_adaptation_inverse_CMCCAT2000():
    def time_sd(self):
        colour.adaptation.chromatic_adaptation_inverse_CMCCAT2000(
            IJK_SD, IJK_SD, IJK_SD, 200, 200)

    def time_hd(self):
        colour.adaptation.chromatic_adaptation_inverse_CMCCAT2000(
            IJK_HD, IJK_HD, IJK_HD, 200, 200)

    def time_uhd(self):
        colour.adaptation.chromatic_adaptation_inverse_CMCCAT2000(
            IJK_UHD, IJK_UHD, IJK_UHD, 200, 200)


class chromatic_adaptation_CMCCAT2000():
    def time_sd(self):
        colour.adaptation.chromatic_adaptation_CMCCAT2000(
            IJK_SD, IJK_SD, IJK_SD, 200, 200)

    def time_hd(self):
        colour.adaptation.chromatic_adaptation_CMCCAT2000(
            IJK_HD, IJK_HD, IJK_HD, 200, 200)

    def time_uhd(self):
        colour.adaptation.chromatic_adaptation_CMCCAT2000(
            IJK_UHD, IJK_UHD, IJK_UHD, 200, 200)
