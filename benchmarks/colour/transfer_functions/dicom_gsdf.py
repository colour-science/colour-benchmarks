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

__all__ = ['DICOM_GSDF_factories']

DICOM_GSDF_factories = {
    'eotf_DICOMGSDF': colour.models.eotf_DICOMGSDF,
    'eotf_inverse_DICOMGSDF': colour.models.eotf_inverse_DICOMGSDF,
}

IJK_benchmark_factory(DICOM_GSDF_factories, __name__)
