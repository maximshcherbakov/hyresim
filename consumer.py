__author__ = 'Nata'

from component import Component
import random
import numpy as np
import pandas as pd
from datetime import datetime, date, time, timedelta

class Consumer(Component):
    """

    """

    power = 0
    typical_daily_on_off_profile = []

    def __init__(self, name_, power_):
        super().__init__(name_)
        self.power = power_
    #     Init the typical_daily_profile
        self.typical_daily_on_off_profile =  pd.DataFrame(np.zeros((96,2)))
        t = datetime(2011,1,1,0, 15)
        iteration_timedelta = timedelta(minutes=15)

        for i in range(len(self.typical_daily_on_off_profile)):
            self.typical_daily_on_off_profile.iloc[i, 0] = t
            t = t + iteration_timedelta
        for i in range(5):
            self.typical_daily_on_off_profile.iloc[40 + i, 1] = 1

        # print(typical_daily_on_off_profile)

    def get_state(self, current_datetime_, **kwargs):
        # todo: max shcherbakov develop the simulation of consumer
        try:
            hour = current_datetime_.hour
            minute = current_datetime_.minute
            # create index using the current_datetime_ and pickup the on/off status from typical_daily_on_off_profile
            t = datetime(2011,1,1,hour, minute)
            # print(self.typical_daily_on_off_profile[t])
            self.state = random.random()
        except:
            print("Error occurs in Component:Consumer. get_state")

        return self.state

