# -*- coding: utf-8 -*-
"""
"colour.colorimetry" sub-package Benchmarks
===========================================
"""

from __future__ import division, unicode_literals

import colour
import numpy as np

from benchmarks.factories.ijk import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = []

prng = np.random.RandomState(2)

M_T_1 = prng.random_sample((345600, 3))
M_R_1 = M_T_1 + (prng.random_sample((345600, 3)) - 0.5) * 0.5
M_T_2 = prng.random_sample((921600, 3))
M_R_2 = M_T_2 + (prng.random_sample((921600, 3)) - 0.5) * 0.5
M_T_3 = prng.random_sample((2073600, 3))
M_R_3 = M_T_3 + (prng.random_sample((2073600, 3)) - 0.5) * 0.5


class ColourCorrectionMatrixFinlayson2015():
    def time_sd(self):
        colour.characterisation.colour_correction_matrix_Finlayson2015(
            M_T_1, M_R_1)

    def time_hd(self):
        colour.characterisation.colour_correction_matrix_Finlayson2015(
            M_T_2, M_R_2)

    def time_uhd(self):
        colour.characterisation.colour_correction_matrix_Finlayson2015(
            M_T_3, M_R_3)


class ColourCorrectionMatrixVandermonde():
    def time_sd(self):
        colour.characterisation.colour_correction_matrix_Vandermonde(
            M_T_1, M_R_1)

    def time_hd(self):
        colour.characterisation.colour_correction_matrix_Vandermonde(
            M_T_2, M_R_2)

    def time_uhd(self):
        colour.characterisation.colour_correction_matrix_Vandermonde(
            M_T_3, M_R_3)


class ColourCorrectionMatrixCheung2004():
    def time_sd(self):
        colour.characterisation.colour_correction_matrix_Cheung2004(
            M_T_1, M_R_1)

    def time_hd(self):
        colour.characterisation.colour_correction_matrix_Cheung2004(
            M_T_2, M_R_2)

    def time_uhd(self):
        colour.characterisation.colour_correction_matrix_Cheung2004(
            M_T_3, M_R_3)


class ColourCorrectionFinlayson2015():
    def time_sd(self):
        colour.characterisation.colour_correction_Finlayson2015(
            M_T_1, M_T_1, M_R_1)

    def time_hd(self):
        colour.characterisation.colour_correction_Finlayson2015(
            M_T_2, M_T_2, M_R_2)

    def time_uhd(self):
        colour.characterisation.colour_correction_Finlayson2015(
            M_T_3, M_T_3, M_R_3)


class ColourCorrectionVandermonde():
    def time_sd(self):
        colour.characterisation.colour_correction_Vandermonde(
            M_T_1, M_T_1, M_R_1)

    def time_hd(self):
        colour.characterisation.colour_correction_Vandermonde(
            M_T_2, M_T_2, M_R_2)

    def time_uhd(self):
        colour.characterisation.colour_correction_Vandermonde(
            M_T_3, M_T_3, M_R_3)


class ColourCorrectionCheung2004():
    def time_sd(self):
        colour.characterisation.colour_correction_Cheung2004(
            M_T_1, M_T_1, M_R_1)

    def time_hd(self):
        colour.characterisation.colour_correction_Cheung2004(
            M_T_2, M_T_2, M_R_2)

    def time_uhd(self):
        colour.characterisation.colour_correction_Cheung2004(
            M_T_3, M_T_3, M_R_3)


class AugmenteMmatrixCheung2004():
    def time_sd(self):
        colour.characterisation.augmented_matrix_Cheung2004(IJK_SD)

    def time_hd(self):
        colour.characterisation.augmented_matrix_Cheung2004(IJK_HD)

    def time_uhd(self):
        colour.characterisation.augmented_matrix_Cheung2004(IJK_UHD)


class PolynomialExpansionVandermonde():
    def time_sd(self):
        colour.characterisation.polynomial_expansion_Vandermonde(IJK_SD)

    def time_hd(self):
        colour.characterisation.polynomial_expansion_Vandermonde(IJK_HD)

    def time_uhd(self):
        colour.characterisation.polynomial_expansion_Vandermonde(IJK_UHD)


class PolynomialExpansionFinlayson2015():
    def time_sd(self):
        colour.characterisation.polynomial_expansion_Finlayson2015(IJK_SD)

    def time_hd(self):
        colour.characterisation.polynomial_expansion_Finlayson2015(IJK_HD)

    def time_uhd(self):
        colour.characterisation.polynomial_expansion_Finlayson2015(IJK_UHD)
