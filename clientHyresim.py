__author__ = 'maxim.shcherbakov'


from datetime import datetime, timedelta
import os

import matplotlib.pyplot as plt

from simulator import Simulator
from hres import HRES
from solarPanel import SolarPanel
from weatherStation import WeatherStation
from htmlLogger import htmlLogger
from consumer import Consumer

from datagen import WeatherDataGenerator

print ("Simulation of Hybrid Renewable Energy Systems")
location = [59.950637, 30.305097]
datetime_simulation_start = datetime(2015, 5, 19, 00, 15)
iteration_timedelta = timedelta(minutes=15)
number_of_iterations = 96
path = os.path.dirname(os.path.realpath(__file__))

lg = htmlLogger(path + '\\report\\hyresim_.html')
lg.appendParagraph("Simulation of Hybrid Renewable Energy Systems")

# Create the weather station
ws = WeatherStation(location)
# Create the HRES
# solar panel (name_, nominal_power_capacity_, temperature_coefficient_)
components_of_HRES = [SolarPanel("Solar Panel # 001", 800, 0.02), Consumer("Main Building")]

#sp = SolarPanel("Thangs Solar Panel", 100)
#components_of_HRES.append(sp)

hres = HRES(components_of_HRES, location)
# default_HRES.print_components_list()
description, simulation_matrix = Simulator.simulate(hres, ws, datetime_simulation_start, iteration_timedelta, number_of_iterations)

lg.appendDataFrame(simulation_matrix)

print(description)
# print(simulation_matrix)

# plt.plot(simulation_matrix.iloc[:,2])
# plt.plot(simulation_matrix.iloc[:,3])
plt.plot(simulation_matrix["Solar Panel # 001"])
plt.plot(simulation_matrix["Main Building"])

plt.savefig(path + '\\report\\demo.png')
lg.appendImage('demo', path + '\\report\\demo.png')
# plt.show()

 #wdg = WeatherDataGenerator()
 #print(wdg.generate())
