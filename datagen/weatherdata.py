__author__ = 'maxim.shcherbakov'

import numpy as np
import pandas as pd

class BasicDataGenerator:

    dataframe = None

    def generate(self):
        dataframe = 5


class WeatherDataGenerator(BasicDataGenerator):
    def generate(self):
        super().generate()
        cols_ = 20
        rows_ = 100
        dataframe = pd.DataFrame(np.zeros((rows_,cols_ )))
        return dataframe


