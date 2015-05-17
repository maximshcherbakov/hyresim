__author__ = 'maxim.shcherbakov'

from src.simulator import Simulator
from src.hres import HRES
from src.solarPanel import SolarPanel
import matplotlib.pyplot as plt


print ("Simulation of Hybrid Renewable Energy Systems")
location = [59.950637, 30.305097]
# Create the HRES
components_of_HRES = []
components_of_HRES.append(SolarPanel("Solar Panel # 0012456", 80))
components_of_HRES.append(SolarPanel("Solar Panel # 5147485", 250))
components_of_HRES.append(SolarPanel("Solar Panel # 5147486", 250))
default_HRES = HRES(components_of_HRES, location)
# default_HRES.print_components_list()

# Make a simulation of created HRES
# Simulator.simulate(default_HRES, 100)
# sim = Simulator("1", "2", 100)
# sim.simulate(default_HRES)
description, simulation_matrix = Simulator.simulate(default_HRES, 96)

print(description)
print(simulation_matrix)

# Visualize the simulation results
print(simulation_matrix.shape[1])
for i in range(1, simulation_matrix.shape[1]):
    plt.plot(simulation_matrix[:, i])

# plt.plot(simulation_matrix[:, 1])
# plt.plot(simulation_matrix[:, 2])
plt.show()



