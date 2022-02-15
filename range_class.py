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
 
        
    def isValueNotInRange(self, parameter_value):
        if parameter_value < self.min:
            return Status_message.LOW_BREACH
        elif parameter_value > self.max:
            return Status_message.HIGH_BREACH
        elif self.warning_flag == True:
            tolerance_value = (self.tolerance/100)*self.max
            if parameter_value <= (self.min+tolerance_value):
                return Status_message.LOW_WARNING
            elif parameter_value >= (self.max-tolerance_value):
                return Status_message.HIGH_WARNING 
        return Status_message.NORMAL
