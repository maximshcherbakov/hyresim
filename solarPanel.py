"""
    Class for implementation of solar panels
    Last changes: 17/5/2015

"""
__author__ = 'maxim.shcherbakov'

import random

from component import Component


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
        """

        :param name_:
        :param power_capacity_:
        :return:
        """
        super().__init__(name_)
        self.power_capacity = power_capacity_

    def get_power(self, solar_irradiance_):
        """
        Obtain the value of state based on calculation of solar_irradiance_. MUST be replaced by correct formula.

        :param solar_irradiance_: float
            Value of solar irradiance that effect to production of solar panels
        """
        # todo : add correct formula
        self.state = solar_irradiance_ * self.power_capacity * random.random()

    def get_state(self, **kwargs):
        try:
            self.get_power(kwargs["solar_irradiance_"])     # solar_irradiance_ taken from **kwargs only
        except:
            print("Failure in get_state: solar_irradiance_ is not in **kwargs")
        return self.state
