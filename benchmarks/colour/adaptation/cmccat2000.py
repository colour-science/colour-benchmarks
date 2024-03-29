# -*- coding: utf-8 -*-
"""
"colour.adaptation" sub-package Benchmarks
==========================================
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


class ChromaticAdaptationForwardCMCCAT2000():
    def time_sd(self):
        colour.adaptation.chromatic_adaptation_forward_CMCCAT2000(
            IJK_SD, IJK_SD, IJK_SD, 200, 200)

    def time_hd(self):
        colour.adaptation.chromatic_adaptation_forward_CMCCAT2000(
            IJK_HD, IJK_HD, IJK_HD, 200, 200)

    def time_uhd(self):
        colour.adaptation.chromatic_adaptation_forward_CMCCAT2000(
            IJK_UHD, IJK_UHD, IJK_UHD, 200, 200)


class ChromaticAdaptationInverseCMCCAT2000():
    def time_sd(self):
        colour.adaptation.chromatic_adaptation_inverse_CMCCAT2000(
            IJK_SD, IJK_SD, IJK_SD, 200, 200)

    def time_hd(self):
        colour.adaptation.chromatic_adaptation_inverse_CMCCAT2000(
            IJK_HD, IJK_HD, IJK_HD, 200, 200)

    def time_uhd(self):
        colour.adaptation.chromatic_adaptation_inverse_CMCCAT2000(
            IJK_UHD, IJK_UHD, IJK_UHD, 200, 200)


class ChromaticAdaptationCMCCAT2000():
    def time_sd(self):
        colour.adaptation.chromatic_adaptation_CMCCAT2000(
            IJK_SD, IJK_SD, IJK_SD, 200, 200)

    def time_hd(self):
        colour.adaptation.chromatic_adaptation_CMCCAT2000(
            IJK_HD, IJK_HD, IJK_HD, 200, 200)

    def time_uhd(self):
        colour.adaptation.chromatic_adaptation_CMCCAT2000(
            IJK_UHD, IJK_UHD, IJK_UHD, 200, 200)
