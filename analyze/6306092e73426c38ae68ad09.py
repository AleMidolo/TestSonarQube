def validate_length_args(self, args):
    """
    Check if value of arguments is not longer than length specified.

    :param args: The received arguments.
    """
    for key, value in args.items():
        if isinstance(value, str) and len(value) > self.max_length:
            raise ValueError(f"The length of '{key}' exceeds the maximum length of {self.max_length}.")