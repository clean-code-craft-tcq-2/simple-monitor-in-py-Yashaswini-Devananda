import enum

class Status_message(enum.IntEnum):
    LOW_BREACH = 0
    HIGH_BREACH = 1
    NORMAL = 2
    LOW_WARNING = 3
    HIGH_WARNING = 4
    
    
class Range:
    def __init__(self, **kwargs):
        self.min = kwargs.get('min', 0)
        self.max = kwargs.get('max', 0)
        self.warning_flag = kwargs.get('warning_flag', False)
        self.tolerance = kwargs.get('tolerance', 0)
 
    def check_for_breach(self, parameter_value):
        message = Status_message.NORMAL
        if parameter_value < self.min:
            message = Status_message.LOW_BREACH
        elif parameter_value > self.max:
            message = Status_message.HIGH_BREACH 
        return message
            
    def check_for_warning(self, parameter_value):
        message = Status_message.NORMAL
        tolerance_value = (self.tolerance/100)*self.max
        if self.warning_flag == True and (parameter_value <= (self.min+tolerance_value)):
            message = Status_message.LOW_WARNING
        elif self.warning_flag == True and (parameter_value >= (self.max-tolerance_value)):
            message = Status_message.HIGH_WARNING 
        return message
        
    def isValueNotInRange(self, parameter_value):
        message = check_for_breach(parameter_value)
        if message == Status_message.NORMAL:
            message = check_for_warning(parameter_value)
        return message

