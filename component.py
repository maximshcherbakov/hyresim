"""

    Module contains class Component
    Last changes: 17/5/2015

"""
__author__ = 'maxim.shcherbakov'


class Component:
    """
    Basic class for components of each HRES 's component

    Attributes
    ----------
    name : String
        Component name

    state : float
        Power consume, produce or store at the certain moment

    """
    name = ""
    state = 0
    description = []

    def __init__(self, name_):
        self.name = name_

    def get_name(self):
        """
        Return name of component.

        :return:
        name : String
            Attribute name
        """
        return self.name

    def get_description(self):
        return self.description

    def get_state(self, current_datetime_, **kwargs):
        """
        Return the state value of component
        :param:
            current_datetime_ : datetime object,
                Current data time stamp where state should be calculated

            **kwargs    : dictionary
                Set of variables obtained to the current datetime

        :return:
        state , float
            Current state of a component. State could be power of consumption, production, charge storage,
            e.g. everything that interested from cost function point of view.
        """
        return self.state
