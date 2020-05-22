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
from colour.models import *

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2019-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'RESOURCES_DIRECTORY', 'IJK_SD', 'IJK_HD', 'IJK_UHD',
    'RGBBenchmarkFactory', 'RGB_benchmark_factory'
]

RESOURCES_DIRECTORY = os.path.join(os.path.dirname(__file__), 'data')

IJK_SD = colour.read_image(os.path.join(RESOURCES_DIRECTORY, 'testImageSD.jpg'))
IJK_HD = colour.read_image(os.path.join(RESOURCES_DIRECTORY, 'testImageHD.jpg'))
IJK_UHD = colour.read_image(os.path.join(RESOURCES_DIRECTORY, 'testImage4K.jpg'))


class RGBBenchmarkFactory(ABC):
    def __init__(self,
                 callable_=lambda x: x,
                 ijk_sd=IJK_SD,
                 ijk_hd=IJK_HD,
                 ijk_uhd=IJK_UHD):
        super().__init__()

        self._callable = callable_
        self._ijk_sd = ijk_sd
        self._ijk_hd = ijk_hd
        self._ijk_uhd = ijk_uhd

    def time_sd(self):
        eval(type(self).__name__)(self._ijk_sd)

    def time_hd(self):
        eval(type(self).__name__)(self._ijk_hd)

    def time_uhd(self):
        eval(type(self).__name__)(self._ijk_uhd)


def RGB_benchmark_factory(factories, modulename=__name__, install=True):
    classes = []
    for factory, callable_ in factories.items():
        class_ = type(factory, (RGBBenchmarkFactory, ),
                      {'_callable': callable_})
        classes.append(classes)

        if install:
            setattr(sys.modules[modulename], '{}_Benchmark'.format(factory),
                    class_)

    return classes
