def get_nested_custom_and_control_args(self, args):
    """
    Split input arguments to control nested and custom.

    Controls arguments: control the IR behavior. These arguments
        will not be put into the spec yml file
    Nested arguments: are used by the Ansible playbooks and will be put
        into the spec yml file.
    Custom arguments: Custom ansible variables to be used instead of the
        normal nested usage.

    :param args: the collected list of args.
    :return: (dict, dict): flat dicts (control_args, nested_args)
    """
    # Initialize return dictionaries
    control_args = {}
    nested_args = {}

    # Iterate through all arguments
    for arg_name, arg_value in args.items():
        # Check if argument is a control argument (starts with '__')
        if arg_name.startswith('__'):
            control_args[arg_name] = arg_value
        # Check if argument is a custom argument (contains ':')
        elif ':' in arg_name:
            # Split the custom argument name and add to nested args
            custom_key = arg_name.replace(':', '.')
            nested_args[custom_key] = arg_value
        # Regular nested argument
        else:
            nested_args[arg_name] = arg_value

    return control_args, nested_args