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

    _tariff = [0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673,
               0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, 0.0673, .0673, 0.0673, 0.0673, 0.0673,
               0.0673, 0.0673, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243,
               0.1243, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893,
               0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893,
               0.0893, 0.0893, 0.0893, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243,
               0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.1243, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893, 0.0893,
               0.0893, 0.0673, 0.0673, 0.0673, 0.0673]

    def __init__(self, daily_prices_):
        self._daily_prices = copy.deepcopy(daily_prices_)

    def get_price(self, iteration_):
        #return 3.5
        return self._tariff[iteration_]
    # def get_price(self, current_observe_datetime_, current_datetime_, iteration_timedelta_):
    #     # return tariff in current time by obtain tariff in position iteration
    #     iteration = (current_observe_datetime_-current_datetime_)/iteration_timedelta_;
    #     return self._tariff[iteration]
    #     kwargs["current_price_"] = prices_.get_price(current_datetime)

    #need to change price to dynamic tariff
    # def get_price(self, iteration_number_):
    #     return self._tariff[iteration_number_]
