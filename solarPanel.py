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
    nominal_power_capacity : float
        Maximal power of Solar Panel
    outdoor_temperature : float
        Temperature of the solar panel
    temperature_coefficient : float
        Temperature coefficient of the solar panel

        Standard condition:
    standard_temperature = 25 C : float
        Temperature in standard condition
    standard_irradiance = 1000 W/m2 : float
        Solar irradiance in standard condition
    """

    nominal_power_capacity = 0
    temperature_coefficient = 0
    standard_temperature = 25
    standard_irradiance = 1000

    def __init__(self, name_, nominal_power_capacity_, temperature_coefficient_):
        """
        :param name_:
        :param nominal_power_capacity_:
        :param temperature_coefficient_:
        :return:
        """
        super().__init__(name_)
        self.nominal_power_capacity = nominal_power_capacity_
        self.temperature_coefficient = temperature_coefficient_

    def get_power(self, solar_irradiance_, outdoor_temperature_):
        """
        Obtain the value of state based on calculation of solar_irradiance_. MUST be replaced by correct formula.

        :param solar_irradiance_: float
            Value of solar irradiance that effect to production of solar panels
        :param outdoor_temperature_
            Value of outdoor temperature that effect to production of solar panels
        """
        # todo : add correct formula
        print("self.nominal_power_capacity_", self.nominal_power_capacity)
        print("solar_irradiance_ ", solar_irradiance_ )
        print("self.temperature_coefficient_ ", self.temperature_coefficient )
        print("outdoor_temperature_ ", outdoor_temperature_ )

        self.state = self.nominal_power_capacity * (solar_irradiance_ / 1000) * (
            1 + self.temperature_coefficient * (outdoor_temperature_ - 25))

    def get_state(self, **kwargs):
        try:
            # todo: FIX THIS ERROR
            self.get_power(kwargs["solar_irradiance_"], kwargs["outdoor_temperature_"])
        except:
            print("Failure in get_state: solar_irradiance_ is not in **kwargs")
        return self.state
