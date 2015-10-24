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
                print("upload battery and consume using grid facilities")
                current_control_signal = 1
                maximum_allowed_charge = battery_blockB.get_maximimal_allowed_charge()
                battery_blockB.set_charge(maximum_allowed_charge)
                current_cost_function = (maximum_allowed_charge + total_consumption) * current_price

        self.control_signals[len(self.control_signals):] = [current_control_signal]
        self.cost_function_values[len(self.cost_function_values):] = [current_cost_function]
        print("--- End manage procedure")


    #Rule-based
    def manage_Rule_based(self, hres_, current_datetime_, **kwargs):
        print("--- Begin manage procedure -- define the control signal using Rule set")

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



        # if total_production >= total_consumption:
        #     print("We generate more than consume")
        #     maximum_allowed_charge = battery_blockA.get_maximimal_allowed_charge()
        #
        #     if total_production > (total_consumption + maximum_allowed_charge):
        #         battery_blockA.set_charge(maximum_allowed_charge)
        #         rest_production = total_production - (total_consumption + maximum_allowed_charge)
        #         current_control_signal = -1
        #         current_cost_function = -1 * rest_production * current_price
        #     else:
        #         rest_production = total_production - total_consumption
        #         current_control_signal = 0
        #         current_cost_function = 0
        #
        #
        # else:
        #     print("We consume  more than generate")
        #     kwargs = {"control_strategy_": 0}
        #     if battery_blockB.get_state(current_datetime_, **kwargs) >= total_consumption:
        #         print("Use all energy in the battery block B")
        #         battery_blockB.set_charge(-total_consumption)
        #         current_control_signal = 0
        #         current_cost_function = 0
        #     else:
        #         print("upload battery and consume using grid fecilities")
        #         current_control_signal = 1
        #         maximum_allowed_charge = battery_blockB.get_maximimal_allowed_charge()
        #         battery_blockB.set_charge(maximum_allowed_charge)
        #         current_cost_function = (maximum_allowed_charge + total_consumption) * current_price

        self.control_signals[len(self.control_signals):] = [current_control_signal]
        self.cost_function_values[len(self.cost_function_values):] = [current_cost_function]
        print("--- End manage procedure")

    pass
