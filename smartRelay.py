__author__ = 'maxim.shcherbakov'


class Relay:

    name = ''

    def __init__(self):
        pass


class BenchmarkControlRelay(Relay):
    """

    """

    control_signals = []


    def modeling_benchmark_control(s_max_A_, charges_A_, s_max_B_, charges_B_, consumption_, pv_generation_, price_, modeling_interval_ = 12):
        _u = [0] * (modeling_interval_-1)
        J = [0] * (modeling_interval_-1)
        # print ("Modeling is started")
        # for t in range(0, modeling_interval_-1):
        #     print ("Step " + str(t) + ";  consumption_= " + str(consumption_[t+1]) + ";  pv_generation_= " +
        #            str(pv_generation_[t+1]) + "; Charge_A_ = " + str(charges_A_[t])+ "; Charge_B_ = " + str(charges_B_[t]))
        #     if pv_generation_[t+1] >= consumption_[t+1]:
        #         print ("We generate more than consume")
        #         if charges_A_[t] + s_max_A_ / 5. <= s_max_A_:
        #             max_allowed_charge = s_max_A_ / 5.
        #         else:
        #             max_allowed_charge = s_max_A_ - charges_A_[t]
        #
        #         if pv_generation_[t+1] >= consumption_[t+1] + max_allowed_charge:
        #             charges_A_[t+1] = charges_A_[t] + max_allowed_charge
        #             rest_generation = pv_generation_[t+1] - max_allowed_charge - consumption_[t+1]
        #             J[t] = -1*rest_generation*price_[t]
        #             u[t] = -1
        #
        #         else:
        #             rest_generation = pv_generation_[t+1] - consumption_[t+1]
        #             u[t] = 0
        #             charges_A_[t+1] = charges_A_[t] + rest_generation
        #             J[t] = 0
        #     else:
        #         print ("We consume  more than generate")
        #         delta_S = consumption_[t+1]
        #         print ("Step " + str(t) + "; Delta_S = " + str(delta_S) + "; Charge = " + str(charges_B_[t]))
        #         print ("s_max_B_/5. = " + str(s_max_B_/5.))
        #
        # #         if (delta_S <= (s_max_B_/5.)) & (charges_B_[t] - delta_S >= (5*s_max_B_/100.)):
        #         if charges_B_[t] - delta_S >= 0:
        #             # consume using battery
        #             print ("Consume using battery")
        #             charges_B_[t+1] = charges_B_[t] - delta_S
        #             _u[t] = 0
        #             J[t] = 0
        #         else:
        #             # upload battery & consume
        #             print ("Upload battery & consume")
        #             _u[t] = 1
        #             charge = s_max_B_ / 5.
        #             if (charges_B_[t] + charge) > s_max_B_:
        #                 charge = s_max_B_ - charges_B_[t]
        #             charges_B_[t+1] = charges_B_[t] + charge
        #             J[t] = (consumption_[t+1]* price_[t+1]) + (charge * price_[t+1])
        #
        # print ("Modeling has finished")
        return J, _u

    def manage(self, hres_, current_datetime_):
        print ("define the control signal")
        current_control_signal = 0
        total_consumption = hres_.get_consumption(current_datetime_)
        total_production = hres_.get_production(current_datetime_)
        print ("Total Consumption: " + str(total_consumption))
        print ("Total Production: " + str(total_production))


        if total_production >= total_consumption:
            print("We generate more than consume")
        else:
            print("We consume  more than generate")

        self.control_signals[len(self.control_signals):] = [current_control_signal]
        pass

    pass