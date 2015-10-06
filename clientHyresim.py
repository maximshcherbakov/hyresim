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
from consumer import ConsumersFactory
from datagen import WeatherDataGenerator
from storageBattery import StorageBattery
from smartRelay import BenchmarkControlRelay


def draw_charts(dataseries_name_, file_name_, xtitle_, ytitle_):
    plt.figure(num=None, figsize=(8, 2), dpi=80, facecolor='w', edgecolor='k')
    plt.plot(simulation_matrix[dataseries_name_])
    plt.suptitle(dataseries_name_, fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=6)
    plt.tick_params(axis='both', which='minor', labelsize=4)
    plt.xlabel(xtitle_, fontsize=8)
    plt.ylabel(ytitle_, fontsize=8)
    plt.savefig(path + '\\report\\' + file_name_ + '.png')

def draw_results():
    draw_charts("Total Consumption", "consumption", "time", "consumption [Wh]")
    lg.appendImage('consumption', path + '\\report\\consumption.png')

    draw_charts("StorageA", "storagea", "time", "capacity [Ah]")
    lg.appendImage('storage', path + '\\report\\storagea.png')

    draw_charts("StorageB", "storageb", "time", "capacity [Ah]")
    lg.appendImage('storage', path + '\\report\\storageb.png')

    draw_charts("Solar Panel", "pv", "time", "PV power [Wh]")
    lg.appendImage('pv', path + '\\report\\pv.png')

    lg.appendDataFrame(simulation_matrix)
    print(description)


# Settings for simulation process
print ("Simulation of Hybrid Renewable Energy Systems")
location = [59.950637, 30.305097]
datetime_simulation_start = datetime(2015, 5, 19, 00, 15)
iteration_timedelta = timedelta(minutes=15)
number_of_iterations = 96 * 2
path = os.path.dirname(os.path.realpath(__file__))

# Creating logger
lg = htmlLogger(path + '\\report\\hyresim_.html')
lg.appendParagraph("Simulation of Hybrid Renewable Energy Systems")

# Create the weather station
ws = WeatherStation(location)

# Create the HRES and its components

# Create consumers
cf = ConsumersFactory()
total_consumption = cf.make_consumer("Total Consumption", 1000, datetime_simulation_start, iteration_timedelta, number_of_iterations)
# kitchen = cf.make_consumer("kitchen", 1000, datetime_simulation_start, iteration_timedelta, number_of_iterations)
# solar panel (name_, nominal_power_capacity_, temperature_coefficient_)
# fridge = Consumer("Main Building", 100, None)

storageA = StorageBattery(name_="StorageA", capacity_=300, charge_=0.5)
storageB = StorageBattery(name_="StorageB", capacity_=300, charge_=0.5)
solar_panel = SolarPanel(name_="Solar Panel", nominal_power_capacity_=800, temperature_coefficient_=0.02, storage_=storageA)
components_of_HRES = [total_consumption, solar_panel, storageA, storageB]
benchmark_relay = BenchmarkControlRelay()
hres = HRES(components_of_HRES, location)

# Create the description of the experiment
lg.append_list_of_paragraphs(ws.get_description())
lg.append_list_of_paragraphs(hres.get_description())

# default_HRES.print_components_list()
description, simulation_matrix = Simulator.simulate(benchmark_relay, hres, ws, datetime_simulation_start, iteration_timedelta, number_of_iterations)
columns = simulation_matrix.columns

# print(columns)
draw_results()
print("Simulation is over")
 #wdg = WeatherDataGenerator()
 #print(wdg.generate())
