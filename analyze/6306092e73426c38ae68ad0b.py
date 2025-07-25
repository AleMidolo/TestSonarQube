def validate_min_max_args(self, args):
    """
    Check if value of arguments is between minimum and maximum values.

    :param args: The received arguments.
    """
    min_value = self.min_value  # Assuming min_value is defined in the class
    max_value = self.max_value  # Assuming max_value is defined in the class
    
    for arg in args:
        if not (min_value <= arg <= max_value):
            raise ValueError(f"Argument {arg} is not between {min_value} and {max_value}.")