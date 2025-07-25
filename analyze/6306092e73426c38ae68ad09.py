def validate_length_args(self, args):
    """
    Check if value of arguments is not longer than length specified.

    :param args: The received arguments.
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, f'max_length_{arg_name}'):
            max_length = getattr(self, f'max_length_{arg_name}')
            if len(arg_value) > max_length:
                raise ValueError(f"Argument '{arg_name}' exceeds maximum length of {max_length}.")