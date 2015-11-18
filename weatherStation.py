"""
    Implementation of WeatherStation
"""
__author__ = 'maxim.shcherbakov'
import csv
import numpy as np
import pandas as pd
from component import Component

class WeatherStation(Component):
    """
    Class for weather station instances. The main responsibility is to provide
    weather data for HRES components on demand

    Parameters
    ----------
    location : list [lat, lon]
        List of longitude and latitude pf HRES position

    Attributes
    ----------
    """

    location = []
    irradiance = []
    temperature = []

    def __init__(self, name_, location_, temperature_profile_, irradiance_profile_):
        print("Weather Station is created")
        # upload weather data from csv file
        self.name = name_
        self.location = location_
        self.irradiance = irradiance_profile_
        self.temperature = temperature_profile_

    def get_description(self):
        """
            Get a list of description of the weather station
        :return:
        """
        description = []
        description.append("Weather Station")
        description.append("Location latitude = " + str(self.location[0]))
        description.append("Location longiude = " + str(self.location[1]))
        return description

    #todo: Include weather data to calculate electricity generation
    def get_weather_conditions(self):
        # Here we need to obtain real values based on location and datetime
        return self.irradiance, self.temperature


class WeatherStationFactory:
    # Create instance of the Class Weather Station
    #5/12/2011
    _irradiance_experiment_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0.0010569, 0.00158535, 0.001849575, 0.0021138, 0.0066173, 0.00886905, 0.009994925,
                                0.0111208, 0.01306595, 0.014038525, 0.014524813, 0.0150111, 0.02436235, 0.029037975,
                                0.031375788, 0.0337136, 0.0368529, 0.03842255, 0.039207375, 0.0399922, 0.0929118,
                                0.1193716, 0.1326015, 0.1458314, 0.11954665, 0.106404275, 0.099833088, 0.0932619,
                                0.05259945, 0.032268225, 0.022102613, 0.011937, 0.011937, 0.011937, 0.011937, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    _temperature_experiment_1 = [1.79742, 1.51794, 1.3782, 1.30833, 1.23846, 0.95898, 0.81924, 0.74937, 0.6795, 0.53334,
                                 0.46026, 0.42372, 0.38718, 0.24102, 0.16794, 0.1314, 0.09486, -0.051305, -0.1243875,
                                 -0.16092875, -0.19747, -0.2991, -0.349915, -0.3753225, -0.40073, -0.50236, -0.553175,
                                 -0.5785825, -0.60399, -0.54221, -0.51132, -0.495875, 0.48043, -0.334295, 0.2612275,
                                 -0.22469375, -0.18816, -0.10223, -0.059265, -0.0377825, -0.0163, 0.1853, 0.2861,
                                 0.3365, 0.3869, 0.547055, 0.6271325, 0.66717125, 0.70721, 1.432405, 1.7950025,
                                 1.97630125, 2.1576, 2.40682, 2.53143, .593735, 2.65604, 2.36727, 2.222885, 2.1506925,
                                 2.0785, 2.0785, 2.0785, 2.0785, 1.69915, 0.699151, 0.69915, 1.69915, 1.31981, 1.31981,
                                 1.31981, 1.31981, 0.94046, 0.94046, 0.94046, 0.94046, 0.56112, 0.56112, 0.56112,
                                 0.56112, 0.18177, 0.18177, 0.18177, 0.18177, -0.19757, -0.19757, -0.19757, -0.19757,
                                 -0.57692, -0.57692, -0.57692, -0.57692, -0.95626, -0.95626, -0.95626, -0.95626]
    #7/7/2011
    _irradiance_experiment_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0152715, 0.02290725, 0.026725125, 0.030543,
                                0.0765285, 0.09952125, 0.111017625, 0.122514, 0.188216, 0.221067, 0.2374925, 0.253918,
                                0.3071245, 0.33372775, 0.347029375, 0.360331, 0.379001, 0.388336, 0.3930035, 0.397671,
                                0.492199, 0.539463, 0.563095, 0.586727, 0.6146355, 0.62858975, 0.635566875, 0.642544,
                                0.684334, 0.705229, 0.7156765, 0.726124, 0.706592, 0.696826, 0.691943, 0.68706,
                                0.697023, 0.7020045, 0.70449525, 0.706986, 0.6409145, 0.60787875, 0.591360875, 0.574843,
                                0.506347, 0.472099, 0.454975, 0.437851, 0.437851, 0.437851, 0.437851, 0.33394, 0.33394,
                                0.33394, 0.33394, 0.164827, 0.164827, 0.164827, 0.164827, 0.068015, 0.068015, 0.068015,
                                0.068015, 0.001702, 0.001702, 0.001702, 0.001702, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0]

    _temperature_experiment_2 = [9.82067, 9.487035, 9.3202175, 9.23680875, 9.1534, 8.81976, 8.65294, 8.56953, 8.48612,
                                 8.701995, 8.8099325, 8.86390125, 8.91787, 8.66868, 8.544085, 8.4817875, 8.41949,
                                 9.296655, 9.7352375, 9.95452875, 10.17382, 12.002265, 12.9164875, 13.37359875,
                                 13.83071, 12.907305, 12.4456025, 12.21475125, 11.9839, 13.62693, 14.448445, 14.8592025,
                                 15.26996, 16.274075, 16.7761325, 17.02716125, 17.27819, 18.15202, 18.588935,
                                 18.8073925, 19.02585, 19.869885, 20.2919025, 20.50291125, 20.71392, 21.31022, 21.60837,
                                 21.757445, 21.90652, 22.42185, 22.679515, 22.8083475, 22.93718, 23.157365, 23.2674575,
                                 23.32250375, 23.37755, 23.427065, 23.4518225, 23.46420125, 23.47658, 23.47658,
                                 23.47658, 23.47658, 23.43444, 23.43444, 23.43444, 23.43444, 22.96818, 22.96818,
                                 22.96818, 22.96818, 21.88708, 21.88708, 21.88708, 21.88708, 20.56715, 20.56715,
                                 20.56715, 20.56715, 19.15476, 19.15476, 19.15476, 19.15476, 17.15343, 17.15343,
                                 17.15343, 17.15343, 15.15211, 15.15211, 15.15211, 15.15211, 13.15079, 13.15079,
                                 13.15079, 13.15079]

    # Experiment 1
    def getWeatherData_1(self, name_, location_, datetime_simulation_start, iteration_timedelta_, number_of_iterations_):
        data_irradiance = np.zeros(number_of_iterations_)
        data_tempearture = np.zeros(number_of_iterations_)
        tmp_dates = []
        current_datetime = datetime_simulation_start
        k = 0
        for i in range(number_of_iterations_):
            data_irradiance[i] = self._irradiance_experiment_1[k]
            data_tempearture[i] = self._temperature_experiment_1[k]
            tmp_dates.append(current_datetime)
            current_datetime += iteration_timedelta_
            k += 1
            if k == number_of_iterations_:
                k = 0

        irradiance_profile = pd.DataFrame(data=data_irradiance, index=tmp_dates, columns=['Irradiance'])
        temperature_profile = pd.DataFrame(data=data_tempearture, index=tmp_dates, columns=['Temperature'])
        WeatherStation_ = WeatherStation(name_, location_, irradiance_profile, temperature_profile)
        return WeatherStation_

    # Experiment 2
    def getWeatherData_2(self, name_, location_, datetime_simulation_start, iteration_timedelta_, number_of_iterations_):
        data_irradiance = np.zeros(number_of_iterations_)
        data_tempearture = np.zeros(number_of_iterations_)
        tmp_dates = []
        current_datetime = datetime_simulation_start
        k = 0
        for i in range(number_of_iterations_):
            data_irradiance[i] = self._irradiance_experiment_2[k]
            data_tempearture[i] = self._temperature_experiment_2[k]
            tmp_dates.append(current_datetime)
            current_datetime += iteration_timedelta_
            k += 1
            if k == number_of_iterations_:
                k = 0

        irradiance_profile = pd.DataFrame(data=data_irradiance, index=tmp_dates, columns=['Irradiance'])
        temperature_profile = pd.DataFrame(data=data_tempearture, index=tmp_dates, columns=['Temperature'])
        WeatherStation_ = WeatherStation(name_, location_, irradiance_profile, temperature_profile)
        return WeatherStation_


    def get_weather_data (self, name_, location_, datetime_simulation_start, iteration_timedelta_, number_of_iterations_):
        data_irradiance = np.zeros(number_of_iterations_)
        data_temperature = np.zeros(number_of_iterations_)
        tmp_dates = []
        tmp_datetime = datetime_simulation_start
        k = 0
        for i in range(number_of_iterations_):
            data_irradiance[i] = self._irradiance_experiment_1[k]
            data_temperature[i] = self._temperature_experiment_1[k]
            tmp_dates.append(tmp_datetime)
            tmp_datetime += iteration_timedelta_
            k += 1
            if k == number_of_iterations_:
                k = 0

        WeatherStation_ = WeatherStation(name_, location_, data_temperature, data_irradiance)
        return WeatherStation_
