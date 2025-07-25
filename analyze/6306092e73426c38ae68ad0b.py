def validate_min_max_args(self, args):
    """
    Check if value of arguments is between minimum and maximum values.

    :param args: The received arguments.
    """
    if not hasattr(self, 'min_value') or not hasattr(self, 'max_value'):
        raise AttributeError("min_value and max_value must be defined in the class.")
    
    for arg in args:
        if not (self.min_value <= arg <= self.max_value):
            raise ValueError(f"Argument {arg} is not between {self.min_value} and {self.max_value}.")