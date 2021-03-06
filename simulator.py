"""
    Simulator class is responsible for management of simulation.
"""
__author__ = 'maxim.shcherbakov'

import numpy as np
import pandas as pd


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
    def simulate(prices_, relay_, hres_, weatherstation_, datetime_simulation_start_, iteration_timedelta_, iterations_=96):
        """
        Simulate HRES.

        :param
        prices_ : instance of _priceGenerator_ class
            Data about electricity price

        relay_ : instanle of _Relay_ class (or its ancestors)
            Manages energy flows and defines a set of control signals

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
        description = hres_.get_components_names()
        description[len(description):] = ["ControlSignal"]
        description[len(description):] = ["CostFunction"]

        overall_consumption = 0
        overall_production = 0

        # Prepare simulation_matrix
        tmp_dates = []
        current_datetime = datetime_simulation_start_
        for i in range(iterations_):
            tmp_dates.append(current_datetime)  # .strftime('%y-%m-%d %hour:%minutes')
            current_datetime += iteration_timedelta_

        simulation_matrix = pd.DataFrame(data= np.zeros ((iterations_, int(hres_.get_components_count()+2) )),
                                         columns=description, index=tmp_dates)

        current_datetime = datetime_simulation_start_

        #todo need to include cost function J and control signals u

        try:
            for iteration in range(iterations_):
                # print("Simulate iteration # " + str(iteration) + " for " + str(current_datetime))
                # simulation_matrix.iloc[iteration, 0] = current_datetime
                kwargs = weatherstation_.get_weather_conditions(current_datetime)
                # get all weather parameters
                kwargs["consumption_"] = hres_.get_consumption(current_datetime)
                # get all consumption to evaluate storage status
                overall_consumption += kwargs["consumption_"]

                kwargs["production_"] = hres_.get_production(current_datetime)
                # get all production to evaluate storage status
                overall_production += kwargs["production_"]

                kwargs["iteration_timedelta_"] = iteration_timedelta_
                kwargs["control_strategy_"] = 0
                kwargs["current_price_"] = prices_.get_price(iteration)

                #kwargs["current_price_"] = prices_.get_price(iterations_)

                relay_.manage(hres_, current_datetime, **kwargs)

                for i, component in enumerate(hres_.get_components()):
                    # print(component.get_name())
                    simulation_matrix.iloc[iteration, i] = component.get_state(current_datetime, **kwargs)
                simulation_matrix.iloc[iteration, hres_.get_components_count()] = relay_.control_signals[len(relay_.control_signals)-1]
                simulation_matrix.iloc[iteration, hres_.get_components_count()+1] = relay_.cost_function_values[len(relay_.cost_function_values)-1]

                current_datetime = current_datetime + iteration_timedelta_
        except:
            print('Error occurs in Simulator.simulate method. Iteration: ' + str(iteration) )

        print ('Overall Consumption = ' + str(overall_consumption) + ' [kW.h]')
        print ('Overall Production = ' + str(overall_production) + ' [kW.h]')
        print('Simulation is done successfully')
        return description, simulation_matrix
