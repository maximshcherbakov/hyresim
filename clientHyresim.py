__author__ = 'maxim.shcherbakov'

from src.simulator import Simulator
from src.hres import HRES, SolarPanel


print ("Simulation of Hybrid Renewable Energy Systems")

location = [59.950637, 30.305097]
components_of_HRES = []

# Add components
components_of_HRES.append(SolarPanel("Solar Panel # 0012456", 80))
components_of_HRES.append(SolarPanel("Solar Panel # 5147485", 250))
components_of_HRES.append(SolarPanel("Solar Panel # 5147486", 250))

default_HRES = HRES(components_of_HRES, location)

default_HRES.print_components_list()

# Simulator.simulate(default_HRES, 100)

sim = Simulator("1", "2", 100)
sim.simulate(default_HRES)