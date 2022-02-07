import battery_param_permssible_range as B1

def isValueNotInRange(parameter_value, min_value, max_value):
    return parameter_value < min_value or parameter_value > max_value # returns true if any 1 con is true

def battery_is_ok(test_data):
    temperatureNotOk = isValueNotInRange(test_data.temperature, B1.battery_temp.min_permissible_value, B1.battery_temp.max_permissible_value)
    socNotOk = isValueNotInRange(test_data.soc, B1.battery_soc.min_permissible_value, B1.battery_soc.max_permissible_value)
    charge_rateNotOk = isValueNotInRange(test_data.charge_rate, B1.battery_charge_rate.min_permissible_value, B1.battery_charge_rate.max_permissible_value)
    return not(temperatureNotOk or socNotOk or charge_rateNotOk)
#     if temperatureNotOk or socNotOk or charge_rateNotOk:
#         return False
#     return True


class Battery_param_limit_test_data:
  def __init__(self, temperature, soc, charge_rate):
    self.temperature = temperature
    self.soc = soc
    self.charge_rate = charge_rate
  
max_temp_check = Battery_param_limit_test_data(B1.battery_temp.max_permissible_value , B1.battery_soc.max_permissible_value, B1.battery_charge_rate.max_permissible_value)
min_temp_check = Battery_param_limit_test_data(B1.battery_temp.min_permissible_value , B1.battery_soc.max_permissible_value, B1.battery_charge_rate.max_permissible_value)
beyond_max_temp_check = Battery_param_limit_test_data((B1.battery_temp.max_permissible_value + 0.1_ , B1.battery_soc.max_permissible_value, B1.battery_charge_rate.max_permissible_value)

if __name__ == '__main__':
  assert(battery_is_ok(beyond_max_temp_check) is False)
#   assert(battery_is_ok(25, 70, 0.7) is True)
#   assert(battery_is_ok(50, 85, 0) is False)
