"""
    Class for implementation of solar panels
    Last changes: 17/5/2015

"""
__author__ = 'maxim.shcherbakov'

from src.component import Component
import random


class SolarPanel(Component):
    """
    Class for Solar Panel Component

    Attributes
    ----------
    power_capacity : float
        Maximal power of Solar Panel
    """
    power_capacity = 0

    def __init__(self, name_, power_capacity_):
        super().__init__(name_)
        self.power_capacity = power_capacity_

    def get_power(self, solar_irradiance_):
        """
        Obtain the value of state based on calculation of solar_irradiance_. MUST be replaced by correct formula.

        :param solar_irradiance_: float
            Value of solar irradiance that effect to production of solar panels
        """
        self.state = solar_irradiance_ * self.power_capacity * random.random()

    @property
    def get_state(self):
        self.get_power(0.25)
        return self.state
