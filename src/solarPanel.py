__author__ = 'maxim.shcherbakov'

from src.component import Component

class SolarPanel(Component):
    """
    Class for Solar Panel Component

    Attributes
    ----------
    power : float
        Maximal power of Solar Panel

    """
    power = 0

    def __init__(self, name_, power_):
        self.name = name_
        self.power = power_

    def get_power(self, solar_irradiance_):
        self.state = solar_irradiance_ * self.power

    @property
    def get_state(self):
        self.get_power(0.25)
        return self.state
