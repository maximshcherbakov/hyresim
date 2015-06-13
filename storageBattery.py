"""
    Contains abstract of Storage Battery instances
"""
__author__ = 'maxim.shcherbakov'

import random
from component import Component


class StorageBattery(Component):
    """

    """
    charge = 1
    capacity = 0  # A capacity of the storage battery [Ah]
    voltage = 24.0  # Voltage on the battery [V]
    nu = 0.85  # Efficiency of Inverter (~0.85)

    def __init__(self, name_, capacity_, charge_):
        # charge -- % of maximal capacity
        super().__init__(name_)
        self.charge = charge_
        self.capacity = capacity_
        self.state = self.capacity * charge_

    def get_state(self, current_datetime, **kwargs):
        # todo: need to be calculaetd based on timedelta_
        time_ = 1  # 15./60.

        try:
            consumption = kwargs["consumption_"]
            # Calculate difference using Peukert Capacity
            delta = (time_ * consumption) / (self.voltage * self.nu)
            self.state = self.state - delta
        except:
            print("Failure in get_state: StorageBattery")
        return self.state
