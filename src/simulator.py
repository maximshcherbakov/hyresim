__author__ = 'maxim.shcherbakov'

class Simulator:

    def __init__(self):
        print("Initialisation of Simulator")

    def simulate(self, _loops = 10):
        print("Start the simulation")

        try:
            for i in range(_loops):
                print("Do iteration = ", i)
        except:
            print("Error occurs in Simulator.simulate method")
        print("Simulation is done sucessfully")


