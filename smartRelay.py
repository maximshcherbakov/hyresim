__author__ = 'maxim.shcherbakov'


class Relay:
    name = ''

    def __init__(self):
        pass


class BenchmarkControlRelay(Relay):
    """

    """

    control_signals = []
    cost_function_values = []

    def modeling_benchmark_control(s_max_A_, charges_A_, s_max_B_, charges_B_, consumption_, pv_generation_, price_,
                                   modeling_interval_=12):
        _u = [0] * (modeling_interval_ - 1)
        J = [0] * (modeling_interval_ - 1)
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

    def manage(self, hres_, current_datetime_, **kwargs):
        print("--- Begin manage procedure -- define the control signal")

        current_control_signal = 0
        current_cost_function = 0
        total_consumption = hres_.get_consumption(current_datetime_)
        total_production = hres_.get_production(current_datetime_)
        print("Total Consumption: " + str(total_consumption))
        print("Total Production: " + str(total_production))

        try:
            current_price = kwargs["current_price_"]
            battery_blockA = hres_.get_component_by_name("StorageA")
            battery_blockB = hres_.get_component_by_name("StorageB")
        except:
            print("Error with TRY block in manage method")
            return

        if battery_blockA == None or battery_blockB == None:
            return
        else:
            print("battery_blockA " + str(battery_blockA.name))
            print("battery_blockB " + str(battery_blockB.name))

        if total_production >= total_consumption:
            print("We generate more than consume")
            maximum_allowed_charge = battery_blockA.get_maximimal_allowed_charge()

            if total_production > (total_consumption + maximum_allowed_charge):
                battery_blockA.set_charge(maximum_allowed_charge)
                rest_production = total_production - (total_consumption + maximum_allowed_charge)
                current_control_signal = -1
                current_cost_function = -1 * rest_production * current_price
            else:
                rest_production = total_production - total_consumption
                current_control_signal = 0
                current_cost_function = 0


        else:
            print("We consume  more than generate")
            kwargs = {"control_strategy_": 0}
            if battery_blockB.get_state(current_datetime_, **kwargs) >= total_consumption:
                print("Use all energy in the battery block B")
                battery_blockB.set_charge(-total_consumption)
                current_control_signal = 0
                current_cost_function = 0
            else:
                print("upload battery and consume using grid fecilities")
                current_control_signal = 1
                maximum_allowed_charge = battery_blockB.get_maximimal_allowed_charge()
                battery_blockB.set_charge(maximum_allowed_charge)
                current_cost_function = (maximum_allowed_charge + total_consumption) * current_price

        self.control_signals[len(self.control_signals):] = [current_control_signal]
        self.cost_function_values[len(self.cost_function_values):] = [current_cost_function]
        print("--- End manage procedure")

    pass
