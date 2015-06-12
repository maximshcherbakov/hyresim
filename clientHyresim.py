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

# Settings for simulation process
print ("Simulation of Hybrid Renewable Energy Systems")
location = [59.950637, 30.305097]
datetime_simulation_start = datetime(2015, 5, 19, 00, 15)
iteration_timedelta = timedelta(minutes=15)
number_of_iterations = 96
path = os.path.dirname(os.path.realpath(__file__))

# Creating logger
lg = htmlLogger(path + '\\report\\hyresim_.html')
lg.appendParagraph("Simulation of Hybrid Renewable Energy Systems")

# Create the weather station
ws = WeatherStation(location)

# Create the HRES
# solar panel (name_, nominal_power_capacity_, temperature_coefficient_)
fridge = Consumer("Main Building", 100)

# Define consumption within all period
tmp_dates = []
current_datetime = datetime_simulation_start
for i in range(number_of_iterations):
    tmp_dates.append(current_datetime)  # .strftime('%y-%m-%d %hour:%minutes')
    current_datetime += iteration_timedelta

print (tmp_dates)


solar_panel = SolarPanel("Solar Panel # 001", 800, 0.02)
components_of_HRES = [solar_panel, fridge]


#sp = SolarPanel("Thangs Solar Panel", 100)
#components_of_HRES.append(sp)

hres = HRES(components_of_HRES, location)

# Create the description of the experiment
lg.append_list_of_paragraphs(ws.get_description())
lg.append_list_of_paragraphs(hres.get_description())

# default_HRES.print_components_list()
description, simulation_matrix = Simulator.simulate(hres, ws, datetime_simulation_start, iteration_timedelta, number_of_iterations)



lg.appendDataFrame(simulation_matrix)
print(description)
# print(simulation_matrix)

# plt.plot(simulation_matrix.iloc[:,2])
# plt.plot(simulation_matrix.iloc[:,3])
# plt.plot(simulation_matrix["Solar Panel # 001"])
# plt.plot(simulation_matrix["Main Building"])
#
# plt.savefig(path + '\\report\\demo.png')
# lg.appendImage('demo', path + '\\report\\demo.png')
# plt.show()

 #wdg = WeatherDataGenerator()
 #print(wdg.generate())
