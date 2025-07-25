def validate_choices_args(self, args):
    """
    Check if value of choice arguments is one of the available choices.

    :param args: The received arguments.
    """
    for arg in args:
        if arg not in self.available_choices:
            raise ValueError(f"Invalid choice: {arg}. Available choices are: {self.available_choices}")