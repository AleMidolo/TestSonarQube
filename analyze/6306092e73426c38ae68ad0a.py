def validate_choices_args(self, args):
    """
    Check if value of choice arguments is one of the available choices.

    :param args: The received arguments.
    """
    for arg_name, arg_value in args.items():
        if arg_name in self.choices:
            if arg_value not in self.choices[arg_name]:
                raise ValueError(f"Invalid choice '{arg_value}' for argument '{arg_name}'. "
                               f"Available choices are: {self.choices[arg_name]}")