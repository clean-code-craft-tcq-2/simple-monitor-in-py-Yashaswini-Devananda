import check_limits
import import battery_param_permssible_range as B1

class Battery_param_limit_test_data:
  def __init__(self, temperature, soc, charge_rate):
  self.temperature = temperature
  self.soc = soc
  self.charge_rate = charge_rate
  
test_data1 = Battery_param_limit_test_data(B1.battery_temp.max_permissible_value , B1.battery_soc.max_permissible_value, battery_charge_rate.max_permissible_value)
  
if __name__ == '__main__':
  assert(battery_is_ok(test_data1) is True)
  print (test_data1)
#   assert(battery_is_ok(50, 85, 0) is False)
