"""
    Simulator class is responsible for management of simulation.
"""
__author__ = 'maxim.shcherbakov'

import numpy as np


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
    def simulate(hres_, iterations_=10):
        """
        Simulate HRES.

        :param
        iterations_: integer, default = 10
            Number of iterations for simulation

        hres_ : HRES()
            An instance of  class: see hres.py. A hybrid renewable energy system for simulation

        :return:
        description : array[1: number_of_components]
            Array with names of components

        simulation_matrix : np.array[number of iterations, number of HRES components + 1]
            Nympy array containing the states for each itearation. The first columns indicates iteration number

        """
        print("Start the simulation")
        description = None
        description = hres_.get_components_names()
        # simulation_matrix = np.zeros((iterations_, hres_.get_components_count()))
        simulation_matrix = np.zeros((iterations_, int(hres_.get_components_count()+1)))

        try:
            for iteration in range(iterations_):
                print("Simulate iteration # ", iteration)
                simulation_matrix[iteration, 0] = iteration
                for i, component in enumerate(hres_.get_components()):
                    simulation_matrix[iteration, i + 1] = component.get_state
        except:
            print('Error occurs in Simulator.simulate method')

        print('Simulation is done successfully')
        return description, simulation_matrix