class BatteryParameter:
    def __init__(self, min_permissible_value, max_permissible_value):
        self.min_permissible_value = min_permissible_value
        self.max_permissible_value = max_permissible_value

battery_temp = BatteryParameter(0, 45)
battery_soc = BatteryParameter(20, 80)
battery_charge_rate = BatteryParameter(0, 0.8)

