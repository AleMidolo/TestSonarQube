def validate_min_max_args(self, args):
    """
    Check if value of arguments is between minimum and maximum values.
    
    :param args: The received arguments.
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'min_{arg_name}') and hasattr(self, f'max_{arg_name}'):
            min_val = getattr(self, f'min_{arg_name}')
            max_val = getattr(self, f'max_{arg_name}')
            
            if not min_val <= arg_value <= max_val:
                raise ValueError(
                    f"Value for {arg_name} must be between {min_val} and {max_val}. "
                    f"Got {arg_value}"
                )