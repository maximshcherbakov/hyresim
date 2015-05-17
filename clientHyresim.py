__author__ = 'maxim.shcherbakov'

from src.simulator import Simulator
from src.hres import HRES
from src.solarPanel import SolarPanel
from src.weatherStation import WeatherStation
import matplotlib.pyplot as plt
from datetime import datetime, date, time, timedelta

print ("Simulation of Hybrid Renewable Energy Systems")
location = [59.950637, 30.305097]
datetime_simulation_start = datetime(2014, 9, 1, 00, 15)
iteration_timedelta = timedelta(minutes=15)
number_of_iterations = 96
# Create the weather station
ws = WeatherStation(location)
# Create the HRES
components_of_HRES = []
components_of_HRES.append(SolarPanel("Solar Panel # 0012456", 80))
components_of_HRES.append(SolarPanel("Solar Panel # 5147485", 250))
components_of_HRES.append(SolarPanel("Solar Panel # 5147486", 250))
hres = HRES(components_of_HRES, location)
# default_HRES.print_components_list()

# Make a simulation of created HRES
# Simulator.simulate(default_HRES, 100)
# sim = Simulator("1", "2", 100)
# sim.simulate(default_HRES)
description, simulation_matrix = Simulator.simulate(hres, ws, datetime_simulation_start, iteration_timedelta, number_of_iterations)

print(description)
print(simulation_matrix)

# tmp = simulation_matrix[1]
# Visualize the simulation results
# print(simulation_matrix.shape[1])
# for i in range(1, simulation_matrix.shape[1]):
#     plt.plot(simulation_matrix[:, i])

# plt.plot(simulation_matrix[:, 1])
plt.plot(simulation_matrix.iloc[:,2])
plt.show()



