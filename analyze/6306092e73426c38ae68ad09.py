def validate_length_args(self, args):
    """
    Check if value of arguments is not longer than length specified.
    
    :param args: The received arguments.
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'{arg_name}_length'):
            max_length = getattr(self, f'{arg_name}_length')
            if isinstance(arg_value, (str, list, dict, tuple)) and len(arg_value) > max_length:
                raise ValueError(f"Length of {arg_name} cannot exceed {max_length} characters")