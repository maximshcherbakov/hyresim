"""
    Simulator class is responsible for management of simulation.
"""
__author__ = 'maxim.shcherbakov'

import numpy as np
import pandas as pd
from datetime import datetime, date, time


class Simulator:
    """
    Simulator of HRES model

    Parameters
    ----------
    datatime_of_simulation_begining : datetime, mandatory
        Date time attribute indicates the start time point of beginning of simulation

    datatime_of_simulation_finishing : datetime, mandatory
        Date time attribute indicates the start time point of beginning of simulation

    step : ineteger
        Step defined as number of seconds

    hres : instance of class 'hres'
        HRES for simulation

    Attributes
    ----------
    timestamp_of_simulation_beginning_ : float,
        Time stamp stands for beginning of simulation.


    """
    timestamp_of_simulation_beginning_ = None
    hres = None

    def __init__(self, datatime_of_simulation_begining, datatime_of_simulation_finishing, step):
        print('Initialisation of Simulator')

    @staticmethod
    def simulate(hres_, weatherstation_, datetime_simulation_start_, iteration_timedelta_, iterations_=96):
        """
        Simulate HRES.

        :param
        hres_ : HRES()
            An instance of  class: see hres.py. A hybrid renewable energy system for simulation

        weatherstation_ : WeatherStation
            An instance of WeatherStation class.

        datetime_simulation_start_ : datetime
            Date time of starting simulation. Use case: datetime_simulation_start = datetime(2014, 9, 1, 00, 15)

        iteration_timedelta_ : timedelta_
            Time delta: time difference between steps of simulations. Use case: iteration_timedelta = timedelta(minutes=15)

        iterations_: integer, default = 96
            Number of iterations for simulation

        :return:
        description : array[1: number_of_components]
            Array with names of components

        simulation_matrix : pd.DataFrame[number of iterations, number of HRES components + datetime]
            Pandas DataFrame containing the states for each itearation. The first columns indicates iteration datetime
            Columns name are equal to Component name

        """
        print("Start the simulation")
        description = None
        description = ['datetime'] + hres_.get_components_names()
        # print(description)
        simulation_matrix = pd.DataFrame(np.zeros((iterations_, int(hres_.get_components_count() + 1))),
                                         columns=description)
        current_datetime = datetime_simulation_start_

        try:
            for iteration in range(iterations_):
                print("Simulate iteration # " + str(iteration) + " for " + str(current_datetime))
                simulation_matrix.iloc[iteration, 0] = current_datetime
                for i, component in enumerate(hres_.get_components()):
                    kwargs = weatherstation_.get_weather_conditions(current_datetime)
                    simulation_matrix.iloc[iteration, i + 1] = component.get_state(**kwargs)
                current_datetime = current_datetime + iteration_timedelta_
        except:
            print('Error occurs in Simulator.simulate method')

        print('Simulation is done successfully')
        return description, simulation_matrix
