class Range:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def isValueNotInRange(self, parameter_value):
        return parameter_value < self.min or parameter_value > self.max # returns true if any 1 con is true
