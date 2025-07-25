def validate_choices_args(self, args):
    """
    Check if value of choice arguments is one of the available choices.

    :param args: The received arguments.
    """
    for arg_name, arg_value in args.items():
        if hasattr(self, arg_name):
            choices = getattr(self, arg_name).choices
            if arg_value not in choices:
                raise ValueError(f"Invalid value for {arg_name}. Expected one of {choices}, got {arg_value}.")