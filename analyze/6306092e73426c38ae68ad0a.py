def validate_choices_args(self, args):
    """
    Check if value of choice arguments is one of the available choices.

    :param args: The received arguments.
    """
    for arg_name, arg_value in args.items():
        if arg_name in self.choices:
            valid_choices = self.choices[arg_name]
            if arg_value not in valid_choices:
                raise ValueError(f"Invalid choice for argument '{arg_name}'. "
                              f"Must be one of: {valid_choices}")