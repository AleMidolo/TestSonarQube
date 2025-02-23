def validate_length_args(self, args):
    """
    Check if value of arguments is not longer than length specified.

    :param args: The received arguments.
    """
    for arg in args:
        if len(arg) > self.max_length:
            raise ValueError(f"Argument '{arg}' exceeds maximum length of {self.max_length}.")