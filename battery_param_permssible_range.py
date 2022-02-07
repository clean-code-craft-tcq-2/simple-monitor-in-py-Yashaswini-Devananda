class BMSParameter:
    def __init__(self, min_permissible_value, max_permissible_value):
        self.min_permissible_value = min_permissible_value
        self.max_permissible_value = max_permissible_value

battery_temp = BMSParameter(0, 45)
battery_soc = BMSParameter(20, 80)
battery_charge_rate = BMSParameter(0, 0.8)

