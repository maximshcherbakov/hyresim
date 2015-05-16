"""
Module contains class Component
"""

__author__ = 'maxim.shcherbakov'


class Component:
    """
    Basic class for components of each HRES's component

    Attributes
    ----------
    name : String
        Component name

    state : float
        Power consume, produce or store at the certain moment

    """
    name = ""
    state = 0


    def __init__(self, name_):
        self.name = name_


    def get_name(self):
        """
        Return 'name' attricbute

        :return:
        name : String
            Attribute name
        """
        return self.name


    def get_state(self):
        return self.state
