"""
    Implementation of WeatherStation
"""
__author__ = 'maxim.shcherbakov'

class WeatherStation():
    """
    Class for weather station instances. The main responsibility is to provide
    weather data for HRES componens on demand

    Parameters
    ----------
    location : list [lat, lon]
        List of longitude and latitude pf HRES position

    Attributes
    ----------
    """
    location = []

    def __init__(self, location_):
        print("Weather Station is created")
        # upload weather data from csv file
        self.location = location_

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


    def get_weather_conditions(self, datetime_):
        # Here we need to obtain real values based on location and datetime
        return {"solar_irradiance_": 0.25, "outdoor_temperature_": -15.2, "humidity": 80}
