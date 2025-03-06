def validate_min_max_args(self, args):
    """
    Check if value of arguments is between minimum and maximum values.

    :param args: The received arguments.
    """
    min_value = 0  # Example minimum value, adjust as needed
    max_value = 100  # Example maximum value, adjust as needed
    
    for arg in args:
        if not (min_value <= arg <= max_value):
            raise ValueError(f"Argument {arg} is not between {min_value} and {max_value}")