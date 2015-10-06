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

    _charging_coefficient = 5.

    low_charge_percentage = 0.1
    consumed = 0

    def __init__(self, name_, capacity_, charge_):
        # charge -- % of maximal capacity
        super().__init__(name_)
        self.charge = charge_
        self.capacity = capacity_
        self.state = self.capacity * charge_
        self.consumed = 0
        self.low_charge_percentage = 0.1

    def get_power(self, current_datetime, **kwargs):
        # todo: need to be calculaetd based on timedelta_
        time_ = 1./4.  # 15./60.
        try:
            consumption = kwargs["consumption_"]
            # Calculate difference using Peukert Capacity
            delta = (time_ * consumption) / (self.voltage * self.nu)

            if (self.state - delta) < self.capacity * self.low_charge_percentage:
                self.state += time_ * 0.1 * self.capacity
                self.consumed += time_ * 0.1 * self.capacity * 220
                print ("Charging at " + str(current_datetime) + '; S = ' + str(time_ * 0.1 * self.capacity) + '; state = ' + str(self.state))
            else:
                self.state = self.state - delta
                print ("Use battery...")
        except:
            print("Failure in get_state: StorageBattery")
        return self.state

    def get_maximimal_allowed_charge(self):
        maximimal_allowed_charge = 0
        default_charge = self.capacity / self._charging_coefficient

        if self.state + default_charge <= self.capacity:
            maximimal_allowed_charge = default_charge
        else:
            maximimal_allowed_charge = self.capacity - self.state
        return maximimal_allowed_charge

    def set_charge(self, charge_amount_):
        """

            Change the state of the battery via charging or discharging by charge_amount_

        :param charge_amount_: (float) amount of charge for charging. If negative, then -- discharge
        :return:
            None
        """
        self.state = self.state + charge_amount_
        if self.state > self.capacity:
            self.state = self.capacity

    def get_state(self, current_datetime, **kwargs):

        """
        Return state of the component
        :return:
        """
        return self.state