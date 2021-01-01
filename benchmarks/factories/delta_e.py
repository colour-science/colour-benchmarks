# -*- coding: utf-8 -*-
"""
Common Benchmark Utilities
==========================
"""

from __future__ import division, unicode_literals

import colour
import os
import sys
from abc import ABC

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2021 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'RESOURCES_DIRECTORY', 'IJK_SD', 'IJK_HD', 'IJK_UHD',
    'DeltaEBenchmarkFactory', 'DeltaE_benchmark_factory'
]

RESOURCES_DIRECTORY = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..', 'data'))
IJK_SD = colour.read_image(
    os.path.join(RESOURCES_DIRECTORY, 'testImageSD.jpg'))
IJK_HD = colour.read_image(
    os.path.join(RESOURCES_DIRECTORY, 'testImageHD.jpg'))
IJK_UHD = colour.read_image(
    os.path.join(RESOURCES_DIRECTORY, 'testImage4K.jpg'))


class DeltaEBenchmarkFactory(ABC):
    def __init__(self):
        super().__init__()

    def _run_callable(self, data, data2):
        if not hasattr(self, '_callable'):
            return

        self._callable(data, data2)

    def time_sd(self):
        self._run_callable(self._ijk_sd, self._ijk_sd)

    def time_hd(self):
        self._run_callable(self._ijk_hd, self._ijk_hd)

    def time_uhd(self):
        self._run_callable(self._ijk_uhd, self._ijk_uhd)


def DeltaE_benchmark_factory(factories, modulename=__name__, install=True):
    classes = []
    for factory, callable_ in factories.items():
        class_ = type(factory, (DeltaEBenchmarkFactory, ), {})
        if type(callable_) == list:
            class_._callable = staticmethod(callable_[0])
            class_._ijk_sd = callable_[1]
            class_._ijk_hd = callable_[2]
            class_._ijk_uhd = callable_[3]
        else:
            class_._callable = staticmethod(callable_)
            class_._ijk_sd = IJK_SD
            class_._ijk_hd = IJK_HD
            class_._ijk_uhd = IJK_UHD
        classes.append(classes)

        if install:
            setattr(sys.modules[modulename], '{}_Benchmark'.format(factory),
                    class_)

    return classes
