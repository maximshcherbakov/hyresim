__author__ = 'Nata'

from component import Component
import random

class Consumer(Component):
    """

    """
    def get_state(self, **kwargs):
        # todo: max shcherbakov develop the simulation of consumer
        self.state = random.random()
        return self.state

