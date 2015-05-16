"""
    HRES - Hybrid renewable system class
"""
__author__ = 'maxim.shcherbakov'

from src.component import Component
from src.solarPanel import SolarPanel

class HRES:
    """
    Parameters
    ----------
    components_list_ : list
        List of HRES components or instances Component class

    location : list [lat, lon]
        List of longitude and latitude pf HRES position

    Attributes
    ----------
    components : list
        List of HRES components or instances Component class

    """
    location = None
    components = []

    def __init__(self, components_list_, location_):
        print('Creating the HRES using list of components')
        self.components = components_list_
        self.location = location_

    def get_components(self):
        return self.components

    def print_components_list(self):
        print('HRES contains on Components:')
        for i, component in enumerate(self.components):
            print("\n", component.get_name())

