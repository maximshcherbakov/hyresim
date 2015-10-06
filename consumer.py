__author__ = 'Nata'

from component import Component
import random
import numpy as np
import pandas as pd
from datetime import datetime, date, time, timedelta

class Consumer(Component):
    """
        Abstract for creating energy consumers
    """

    power = 0   # maximal power of the component [W]
    # the Pandas Series of consumption during the simulation period.
    # Indecies indicates the timestamps, and the data is energy consumed during the timedelta
    # Column for data is named 'Consumption'

    # _state_ indicates the power used durint deltatime [W]

    consumption_profile = None


    def __init__(self, name_, power_, consumption_profile_):
        super().__init__(name_)
        self.power = power_
        self.consumption_profile = consumption_profile_

    def get_state(self, current_datetime_, **kwargs):
        # todo: max shcherbakov develop the simulation of consumer
        try:
            # Try to get the consumption for current _datetime_ in the consumption_profile
            self.state = self.consumption_profile['Consumption'][current_datetime_]
        except:
            print("Error occurs in Component:Consumer. get_state")
            self.state = random.random()
        return self.state


class ConsumersFactory():
    """
        Creates the instance of the Class Consumer
    """
    profile = [0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,
               0,0,0,0,0,0,0,0,0,0,
                0,0]

    def make_consumer(self, name_, power_, datetime_simulation_start, iteration_timedelta_, number_of_iterations_):
        # consumption_profile = []
        data_ = np.zeros(number_of_iterations_)
        for i in range(number_of_iterations_):
            data_[i] = 250 * random.uniform(0.9, 1.1)
        # for i in range(36, 46):
        #     data_[i] = 1500* random.uniform(0.9, 1.1)
        # for i in range(46, 57):
        #     data_[i] = 1000* random.uniform(0.9, 1.1)
        # for i in range(57, 72):
        #     data_[i] = 1200* random.uniform(0.9, 1.1)
        # for i in range(72, 84):
        #     data_[i] = 1000* random.uniform(0.9, 1.1)
        #
        # weekend_data_ = np.zeros(96)
        # for i in range(96):
        #     weekend_data_[i] = 250 * random.uniform(0.9, 1.1)
        #
        # data_2 = weekend_data_
        # number_of_days = int(number_of_iterations_/96)
        # for days in range(number_of_days - 2):
        #     data_2 = np.concatenate((data_2, data_))
        #
        # data_2 = np.concatenate((data_2, weekend_data_))
        #
        # # Define consumption within all period
        tmp_dates = []
        current_datetime = datetime_simulation_start
        for i in range(number_of_iterations_):
            tmp_dates.append(current_datetime)
            current_datetime += iteration_timedelta_
        consumption_profile = pd.DataFrame(data=data_, index=tmp_dates, columns=['Consumption'])
        # Randomly set up the values
        #
        # for i in range(number_of_iterations_):
        #     consumption_profile['Consumption'][i] = 250 * random.uniform(0.9, 1.1)
        # for i in range(36, 46):
        #     consumption_profile['Consumption'][i] = 1500* random.uniform(0.9, 1.1)
        # for i in range(46, 57):
        #     consumption_profile['Consumption'][i] = 1000* random.uniform(0.9, 1.1)
        # for i in range(57, 72):
        #     consumption_profile['Consumption'][i] = 1200* random.uniform(0.9, 1.1)
        # for i in range(72, 84):
        #     consumption_profile['Consumption'][i] = 1000* random.uniform(0.9, 1.1)

        # consumption_profile['Consumption'] = consumption_profile['Consumption'] * random.uniform(0.9, 1.1)
        # print(consumption_profile)
        # Create the consumer instance
        consumer = Consumer(name_, power_, consumption_profile)
        return consumer