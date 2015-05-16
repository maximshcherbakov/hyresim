"""Simulator class is responsible for management of simulation.

"""
__author__ = 'maxim.shcherbakov'

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

    Attributes
    ----------
    timestamp_of_simulation_beginning_ : float,
        Time stamp stands for beginning of simulation.

    """
    timestamp_of_simulation_beginning_ = None

    def __init__(self, datatime_of_simulation_begining, datatime_of_simulation_finishing, step):
        print("Initialisation of Simulator")

    def simulate(self, _loops = 10):
        """

        :param
            _loops: integer, default = 10
                Number of loops for simulation
        :return:
            None
        """
        print("Start the simulation")

        try:
            for i in range(_loops):
                print("Do iteration = ", i)
        except:
            print("Error occurs in Simulator.simulate method")
        print("Simulation is done sucessfully")


