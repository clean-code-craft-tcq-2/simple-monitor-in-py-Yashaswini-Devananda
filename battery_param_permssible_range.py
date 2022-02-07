class BMSParameter:
    min_permissible_value = 0
    max_permissible_value = 0

battery_temp = BMSParameter()
battery_temp.min_permissible_value = 0
battery_temp.max_permissible_value = 45

battery_soc = BMSParameter()
battery_soc.min_permissible_value = 20
battery_soc.max_permissible_value = 80

battery_charge_rate = BMSParameter()
battery_charge_rate.min_permissible_value = 0
battery_charge_rate.max_permissible_value = 0.8
