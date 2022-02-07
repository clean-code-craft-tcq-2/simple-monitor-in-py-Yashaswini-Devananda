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

def isValueNotInRange(parameter_value, min_value, max_value):
    return parameter_value < min_value or parameter_value > max_value # returns true if any 1 con is true

def battery_is_ok(temperature, soc, charge_rate):
    temperatureNotOk = isValueNotInRange(temperature, battery_temp.min_permissible_value, battery_temp.max_permissible_value)
    socNotOk = isValueNotInRange(soc, battery_soc.min_permissible_value, battery_soc.max_permissible_value)
    charge_rateNotOk = isValueNotInRange(charge_rate, battery_charge_rate.min_permissible_value, battery_charge_rate.max_permissible_value)
    if temperatureNotOk or socNotOk or charge_rateNotOk:
        return False
    else:
        return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
