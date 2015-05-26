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
    surface_temperature : float
        Surface temperature of the solar panel
    temperature_coefficient : float
        Temperature coefficient of the solar panel

        Standard condition:
    standard_temperature = 25 C : float
        Temperature in standard condition
    standard_irradiance = 1000 W/m2 : float
        Solar irradiance in standard condition
    """
    nominal_power_capacity = 0
    surface_temperature = 0
    temperature_coefficient = 0
    standard_temperature = 25
    standard_irradiance = 1000

    def __init__(self, name_, nominal_power_capacity_, surface_temperature_, temperature_coefficient_, standard_temperature_, standard_irradiance_):
        """

        :param name_:
        :param nominal_power_capacity_:
        :param surface_temperature_:
        :param temperature_coefficient_:
        :param standard_temperature_:
        :param standard_irradiance_:
        :return:
        """
        super().__init__(name_)
        self. nominal_power_capacity = nominal_power_capacity_
        self.surface_temperature = surface_temperature_
        self.temperature_coefficient = temperature_coefficient_
        self.standard_temperature = standard_temperature_
        self.standard_irradiance = standard_irradiance_

    def get_power(self, solar_irradiance_, surface_temperature_, temperature_coefficient_, standard_temperature_, standard_irradiance_):
        """
        Obtain the value of state based on calculation of solar_irradiance_. MUST be replaced by correct formula.

        :param solar_irradiance_: float
            Value of solar irradiance that effect to production of solar panels

        We use function f(x)=sin(x)*random() to simulate the change of the generation electricity from solar panel
        due to time of the day
        """
        # todo : add correct formula

        self.state = self.nominal_power_capacity_ * (solar_irradiance_ / standard_irradiance_ ) *(1 + temperature_coefficient_ * (surface_temperature_ - standard_temperature_ )) * random.random()

    def get_state(self, **kwargs):
        try:

            # Need to fix this error

            self.get_power(kwargs["solar_irradiance_", "surface_temperature_", "temperature_coefficient_", "standard_temperature_", "standard_irradiance_"])
            #, kwargs["surface_temperature_"], kwargs["temperature_coefficient_"], kwargs["standard_temperature_"], kwargs["standard_irradiance_"])     # solar_irradiance_ taken from **kwargs only
        except:
            print("Failure in get_state: solar_irradiance_ is not in **kwargs")
        return self.state
