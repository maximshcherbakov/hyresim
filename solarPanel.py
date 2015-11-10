"""
    Class for implementation of solar panels and storage block A
    Last changes: 17/5/2015

"""
__author__ = 'maxim.shcherbakov'

import random
import numpy as np
import pandas as pd
from component import Component
from storageBattery import StorageBattery

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

    production_profile = None

    nominal_power_capacity = 0
    temperature_coefficient = 0
    standard_temperature = 25
    standard_irradiance = 1000

    _storage = None

    def __init__(self, name_, production_profile_):
        """
        :param name_:
        :param nominal_power_capacity_:
        :param temperature_coefficient_:
        :param storage_: is the object of  StorageBattery class which is represents Storage Block B

        :return:
        """
        super().__init__(name_)
        self.production_profile = production_profile_


    # def __init__(self, name_, nominal_power_capacity_, temperature_coefficient_, production_profile_, storage_ = None):
    #     """
    #     :param name_:
    #     :param nominal_power_capacity_:
    #     :param temperature_coefficient_:
    #     :param storage_: is the object of  StorageBattery class which is represents Storage Block B
    #
    #     :return:
    #     """
    #     super().__init__(name_)
    #     self.nominal_power_capacity = nominal_power_capacity_
    #     self.temperature_coefficient = temperature_coefficient_
    #     self._storage = storage_
    #     self.production_profile = production_profile_

    def get_power(self, solar_irradiance_, outdoor_temperature_):
        """
        Obtain the value of state based on calculation of solar_irradiance_. MUST be replaced by correct formula.

        :param solar_irradiance_: float
            Value of solar irradiance that effect to production of solar panels
        :param outdoor_temperature_
            Value of outdoor temperature that effect to production of solar panels
        """
        # todo : add correct formula
        # print("self.nominal_power_capacity_", self.nominal_power_capacity)
        # print("solar_irradiance_ ", solar_irradiance_ )
        # print("self.temperature_coefficient_ ", self.temperature_coefficient )
        # print("outdoor_temperature_ ", outdoor_temperature_ )

        self.state = self.nominal_power_capacity * (solar_irradiance_ / 1000) * (
            1 + self.temperature_coefficient * (outdoor_temperature_ - 25))

    def get_state(self, current_datetime_, **kwargs):
        # try:
        #     # todo: FIX THIS ERROR
        #     self.get_power(kwargs["solar_irradiance_"], kwargs["outdoor_temperature_"])
        # except:
        #     print("Failure in get_state: solar_irradiance_ is not in **kwargs")
        # return self.state

        try:
            # Try to get the consumption for current _datetime_ in the consumption_profile
            self.state = self.production_profile['Production'][current_datetime_]

        except:
            print("Error occurs in Component:Production. get_state")
            self.state = random.random()
        return self.state


    def make_producer(name_, datetime_simulation_start, iteration_timedelta_, number_of_iterations_):
        data_ = np.zeros(number_of_iterations_)
        for i in range(number_of_iterations_):
            data_[i] = 250 * random.uniform(0.9, 1.1)
        tmp_dates = []
        current_datetime = datetime_simulation_start
        for i in range(number_of_iterations_):
            tmp_dates.append(current_datetime)
            current_datetime += iteration_timedelta_
        consumption_profile = pd.DataFrame(data=data_, index=tmp_dates, columns=['Consumption'])
        solarPanel_ = SolarPanel(name_, consumption_profile)
        return solarPanel_

class ProductionFactory:
    #5/12/2011
    _profile_production_experiment_1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                0.1057, 1.4744, 2.3939, 3.8211, 11.8817, 11.0649, 11.3693, 9.4373, 11.7325, 12.1587,
                                14.723, 9.4681, 10.0964, 10.2821, 16.7039, 29.6371, 18.7177, 22.0234, 25.2014,
                                23.0188, 19.4218, 12.6238, 9.4799, 11.1222, 5.1241, 3.8932, 5.5004, 3.6354,
                                1.6375, 0.5586, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #7/7/2011
    _profile_production_experiment_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0.2423, 1.2195, 1.1014, 2.2434, 2.5420, 3.0339, 3.4505, 3.7830, 1.0355,
                            11.5190, 22.9070, 34.8225, 62.2720, 50.1450, 58.4945, 47.8915, 49.5240, 57.2165,
                            109.7420, 110.6105, 81.3685, 128.6275, 77.7145, 44.2955, 112.7305, 71.6815, 18.9920,
                            18.1655, 34.4205, 33.8490, 34.7380, 8.4680, 1.4320, 2.1580, 16.0740, .0068, 2.1898,
                            1.3579, 1.1713, 0.7163, 0.2889, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                            0, 0, 0, 0, 0, 0, 0]

    def make_production_experiment_1(self, name_, power_, datetime_simulation_start, iteration_timedelta_, number_of_iterations_):

        data_ = np.zeros(number_of_iterations_)
        tmp_dates = []
        current_datetime = datetime_simulation_start
        k = 0
        for i in range(number_of_iterations_):
            data_[i] = self._profile_production_experiment_1[k]
            tmp_dates.append(current_datetime)
            current_datetime += iteration_timedelta_
            k+=1
            if k == len(self._profile_production_experiment_1):
                k = 0
        production_profile = pd.DataFrame(data=data_, index=tmp_dates, columns=['Production'])
        solar_panel_1 = SolarPanel(name_, production_profile)
        return solar_panel_1

    def make_production_experiment_2(self, name_, power_, datetime_simulation_start, iteration_timedelta_, number_of_iterations_):

        data_ = np.zeros(number_of_iterations_)
        tmp_dates = []
        current_datetime = datetime_simulation_start
        k = 0
        for i in range(number_of_iterations_):
            data_[i] = self._profile_production_experiment_2[k]
            tmp_dates.append(current_datetime)
            current_datetime += iteration_timedelta_
            k+=1
            if k == len(self._profile_production_experiment_2):
                k = 0
        production_profile = pd.DataFrame(data=data_, index=tmp_dates, columns=['Consumption in 1st experiment'])
        solar_panel_2 = SolarPanel(name_, production_profile)
        return solar_panel_2