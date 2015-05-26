"""
    Contains abstract of Storage Battery instances
"""
__author__ = 'maxim.shcherbakov'

from component import Component

class StorageBattery(Component):
    """

    """
    charge = 0

    def get_state(self, **kwargs):
        # todo: max shcherbakov, develop the simulation of Storage Battery
        return 10

