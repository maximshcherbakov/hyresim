"""
    Simulator class is responsible for management of simulation.
"""
__author__ = 'maxim.shcherbakov'

from src.hres import Component
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
        Simulate HRES

        :param
            iterations_: integer, default = 10
                Number of iterations for simulation
        :return:
            None
        """
        print("Start the simulation")

        try:
            for iteration in range(iterations_):
                print("Do iteration = ", iteration)
                for i, component in enumerate(hres_.get_components()):
                    print(component.get_name() + " has " + str(component.get_state) + " W")

        except:
            print("Error occurs in Simulator.simulate method")
        print("Simulation is done sucessfully")


