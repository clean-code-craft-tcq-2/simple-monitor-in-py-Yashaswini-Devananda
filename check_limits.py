import range_class
import enum

english_messages = {"LOW_BREACH" : "LOW BREACH",
"HIGH_BREACH" : "HIGH BREACH",
"NORMAL" : "NORMAL",
"LOW_WARNING" : "LOW WARNING",
"HIGH_WARNING" : "HIGH WARNING",
"temperature" : "Temperature",
"soc" : "SOC",
"charge_rate" : "Charge rate"
}

kannada_messages = {"LOW_BREACH" : "Kaḍime ullaṅghane",
"HIGH_BREACH" : "Hecchu ullaṅghane",
"NORMAL" : "sari ide",
"LOW_WARNING" : "kadime eccharike",
"HIGH_WARNING" : "Hecchu eccharike",
"temperature" : "Taapamana",
"soc" : "SOC",
"charge_rate" : "Charge ratuuu"
}

class Language(enum.IntEnum):
    english = 0
    kannada = 1
    
language_list = [english_messages, kannada_messages]
selected_language = Language.kannada # english

    
def look_up_dictionary(message):
    return f"{language_list[selected_language][message]}"


class Status_message(enum.IntEnum):
    LOW_BREACH = 0
    HIGH_BREACH = 1
    NORMAL = 2
    LOW_WARNING = 3
    HIGH_WARNING = 4
    

battery = []
battery.append(range_class.Range(min= 10, max = 100, warning_flag = False, tolerance = 5)) # temperature
battery.append(range_class.Range(min= 20, max = 80)) # soc
battery.append(range_class.Range(min= 0, max = 0.8, warning_flag = True, tolerance = 5)) # charge rate

class Param(enum.IntEnum):
    temperature = 0
    soc = 1
    charge_rate = 2
    parameter_count = 3 # increment this if a parameter is added
    
    
    
def battery_is_ok(battery_status):
    print ("")
    print (battery_status)
    for x in range (Param.parameter_count):
        parameter_status = battery[x].isValueNotInRange(battery_status[x])
        print (f"{look_up_dictionary(Param(x).name)} {look_up_dictionary(Status_message(parameter_status).name)}")
        if parameter_status.value <= 1:
            return False
    return True

if __name__ == '__main__':
    # print ("[temperature, soc, charge_rate] : Battery State")
    battery_status = [9,25,0.7] #temperature, soc, charge_rate
    # print(battery_is_ok(battery_status))
    
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
        
        battery_status[i] = battery[i].min+((20/100)*battery[i].max)
        assert(battery_is_ok(battery_status) is True)
        
        battery_status[i] = battery[i].max+0.1
        assert(battery_is_ok(battery_status) is False)
        
        battery_status[i] = battery[i].min-0.1
        assert(battery_is_ok(battery_status) is False)
