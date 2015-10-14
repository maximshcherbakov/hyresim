__author__ = 'maxim.shcherbakov'

import copy


class priceGenerator:
    """
        Contains information about daily electricity price

    Attributes
    ----------
    _daily_prices : pandas dataframe
        Contains daily price

    """

    _daily_prices = None

    def __init__(self, daily_prices_):
        self._daily_prices = copy.deepcopy(daily_prices_)

    def get_price(self, current_datetime_):
        return 3.5
