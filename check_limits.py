import range_class as Range
import enum

battery = []
battery.append(Range(0, 45)) # temperature
battery.append(Range(20, 80)) # soc
battery.append(Range(0, 0.8)) # charge_rate

class Param(enum.IntEnum):
    temperature = 0
    soc = 1
    charge_rate = 2
    parameter_count = 3 # increment this if a parameter is added
    

def battery_is_ok(battery_status):
    temperatureNotOk = battery[Param.temperature].isValueNotInRange(battery_status[Param.temperature])
    socNotOk = battery[Param.soc].isValueNotInRange(battery_status[Param.soc])
    charge_rateNotOk = battery[Param.charge_rate].isValueNotInRange(battery_status[Param.charge_rate])
    return_value = not(temperatureNotOk or socNotOk or charge_rateNotOk)
    ok = "ok"
    NotOK = "NotOK"
    print (f"{battery_status} : {(NotOK,ok) [return_value]}")
    return return_value


if __name__ == '__main__':
    print ("[temperature, soc, charge_rate] : Battery State")
    battery_status = [0,0,0] #temperature, soc, charge_rate
    
    for i in range(Param.parameter_count):
        for j in range(Param.parameter_count):
            if j!=i:
                battery_status[j] = battery[j].max
                
                
        battery_status[i] = battery[i].max
        assert(battery_is_ok(battery_status) is True)
        
        battery_status[i] = battery[i].min
        assert(battery_is_ok(battery_status) is True)
        
        battery_status[i] = battery[i].max-0.1
        assert(battery_is_ok(battery_status) is True)
        
        battery_status[i] = battery[i].min+0.1
        assert(battery_is_ok(battery_status) is True)
        
        battery_status[i] = battery[i].max+0.1
        assert(battery_is_ok(battery_status) is False)
        
        battery_status[i] = battery[i].min-0.1
        assert(battery_is_ok(battery_status) is False)
