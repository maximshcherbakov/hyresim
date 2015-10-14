__author__ = 'Nata'

import random

import numpy as np
import pandas as pd

from component import Component


class Consumer(Component):
    """
        Abstract for creating energy consumers
    """

    power = 0  # maximal power of the component [W]
    # the Pandas Series of consumption during the simulation period.
    # Indexes indicates the timestamps, and the data is energy consumed during the timedelta
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


def make_consumer(name_, power_, datetime_simulation_start, iteration_timedelta_, number_of_iterations_):
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


class ConsumersFactory:
    """
        Creates the instance of the Class Consumer
    """

    _profile_consumption_1 = [17.256, 17.1628, 17.0789, 16.2376, 16.7697, 16.7727, 17.2507, 18.4293, 16.0598, 16.9976,
                              16.2851, 17.6931, 17.5741, 16.4008, 15.8628, 17.2796, 16.2484, 17.4169, 16.1351, 16.0802,
                              16.9067, 16.9072, 16.4614, 17.3846, 16.687, 16.1185, 16.5016, 17.1023, 16.9477, 17.2466,
                              16.3577, 17.8381, 16.6401, 16.8081, 16.4357, 16.848, 16.0599, 16.5646, 16.9363, 16.5161,
                              16.0006, 16.7092, 16.5884, 16.6571, 16.5663, 16.6903, 16.5958, 16.63, 16.671, 17.0847,
                              16.5221, 16.6127, 16.6176, 17.0544, 16.9716, 16.9032, 17.3345, 16.7972, 15.9917, 16.2279,
                              17.1029, 16.978, 16.0205, 16.591, 15.8056, 16.7583, 17.1577, 15.7867, 16.7734, 16.2602,
                              16.8079, 15.964, 16.7803, 16.4572, 16.3126, 16.8357, 18.7196, 15.9033, 15.8696, 17.2444,
                              16.7664, 15.8081, 16.8318, 16.6988, 16.6816, 16.5235, 16.3746, 15.9147, 16.8162, 16.4219,
                              16.4129, 16.3233, 16.0406, 16.9449, 17.2333, 15.8762]

    _profile_consumption_2 = [16.2534, 16.3538, 16.2126, 16.3945, 16.1535, 16.005, 16.3083, 16.4135, 15.8802, 16.419,
                              16.7622,
                              15.8651, 18.6612, 6.7369, 15.9894, 16.1309, 17.5289, 15.6967, 15.7476, 16.6705, 15.8501,
                              15.709,
                              16.4266, 16.2667, 16.2849, 16.1913, 16.4363, 16.6859, 15.8123, 48.2695, 70.9055, 70.3771,
                              66.2131,
                              61.6494, 63.9941, 65.5227, 79.497, 87.4764, 83.2983, 104.3891, 112.4102, 104.629,
                              106.6512, 104.1421,
                              108.1597, 108.0424, 112.7142, 112.1556, 112.0111, 111.7143, 108.8681, 106.8629, 109.5954,
                              110.7905,
                              109.8269, 108.9871, 106.9269, 109.6012, 109.8441, 106.53, 109.6796, 101.2342, 108.907,
                              109.4964,
                              109.3118, 109.0647, 106.2338, 102.2167, 105.9839, 96.7221, 97.3943, 84.9826, 76.427,
                              77.6324, 64.2577,
                              22.5289, 13.0356, 18.0735, 17.7837, 15.6354, 15.9784, 15.9706, 15.2587, 15.1443, 15.0352,
                              16.3814,
                              14.7429, 16.6681, 16.3867, 16.7962, 16.7591, 16.8593, 16.7696, 16.7833, 17.2674, 17.6232]

    def make_consumer_experiment1(self, name_, power_, datetime_simulation_start, iteration_timedelta_,
                                  number_of_iterations_):

        data_ = np.zeros(number_of_iterations_)
        tmp_dates = []
        current_datetime = datetime_simulation_start
        k = 0
        for i in range(number_of_iterations_):
            data_[i] = self._profile_consumption_1[k]
            tmp_dates.append(current_datetime)
            current_datetime += iteration_timedelta_
            k += 1
            if k == len(self._profile_consumption_1):
                k = 0

        # Thang, please be careful with the name of column
        consumption_profile = pd.DataFrame(data=data_, index=tmp_dates, columns=['Consumption'])
        consumer = Consumer(name_, power_, consumption_profile)
        return consumer

    def make_consumer_experiment2(self, name_, power_, datetime_simulation_start, iteration_timedelta_,
                                  number_of_iterations_):

        data_ = np.zeros(number_of_iterations_)
        tmp_dates = []
        current_datetime = datetime_simulation_start
        k = 0
        for i in range(number_of_iterations_):
            data_[i] = self._profile_consumption_2[k]
            tmp_dates.append(current_datetime)
            current_datetime += iteration_timedelta_
            k += 1
            if k == len(self._profile_consumption_2):
                k = 0
        consumption_profile = pd.DataFrame(data=data_, index=tmp_dates, columns=['Consumption'])
        consumer_1 = Consumer(name_, power_, consumption_profile)
        return consumer_1
