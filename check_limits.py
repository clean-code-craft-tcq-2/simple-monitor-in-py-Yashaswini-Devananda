import battery_param_permssible_range as B1

def isValueNotInRange(parameter_value, min_value, max_value):
    return parameter_value < min_value or parameter_value > max_value # returns true if any 1 con is true

def battery_is_ok(temperature, soc, charge_rate):
    temperatureNotOk = isValueNotInRange(temperature, B1.battery_temp.min_permissible_value, B1.battery_temp.max_permissible_value)
    socNotOk = isValueNotInRange(soc, B1.battery_soc.min_permissible_value, B1.battery_soc.max_permissible_value)
    charge_rateNotOk = isValueNotInRange(charge_rate, B1.battery_charge_rate.min_permissible_value, B1.battery_charge_rate.max_permissible_value)
    return not(temperatureNotOk or socNotOk or charge_rateNotOk)
#     if temperatureNotOk or socNotOk or charge_rateNotOk:
#         return False
#     return True

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
