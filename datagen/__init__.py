"""
The :mod:`hyresim.datagen` module implements the generation of different types of data.
"""

__author__ = 'maxim.shcherbakov'

from .weatherdata import BasicDataGenerator
from .weatherdata import WeatherDataGenerator


__all__ = ['BasicDataGenerator',
           'WeatherDataGenerator']