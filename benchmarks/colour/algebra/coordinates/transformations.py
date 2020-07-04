# -*- coding: utf-8 -*-
"""
"colour.algebra" sub-package Benchmarks
=======================================
"""

from __future__ import division, unicode_literals

import colour
import numpy as np

from benchmarks.factories.ijk import IJK_benchmark_factory
from benchmarks.factories.ijk import IJK_SD, IJK_HD, IJK_UHD

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = ['TransformationsFactories']

IJK_SD_POLAR = np.ones(shape=(IJK_SD.shape[0], IJK_SD.shape[1], 2))
IJK_HD_POLAR = np.ones(shape=(IJK_HD.shape[0], IJK_HD.shape[1], 2))
IJK_UHD_POLAR = np.ones(shape=(IJK_UHD.shape[0], IJK_UHD.shape[1], 2))

TransformationsFactories = {
    'cartesian_to_spherical':
    colour.algebra.cartesian_to_spherical,
    'spherical_to_cartesian':
    colour.algebra.spherical_to_cartesian,
    'cartesian_to_polar': [
        colour.algebra.cartesian_to_polar, IJK_SD_POLAR, IJK_HD_POLAR,
        IJK_UHD_POLAR
    ],
    'polar_to_cartesian': [
        colour.algebra.polar_to_cartesian, IJK_SD_POLAR, IJK_HD_POLAR,
        IJK_UHD_POLAR
    ],
    'cartesian_to_cylindrical':
    colour.algebra.cartesian_to_cylindrical,
    'cylindrical_to_cartesian':
    colour.algebra.cylindrical_to_cartesian,
}

IJK_benchmark_factory(TransformationsFactories, __name__)
