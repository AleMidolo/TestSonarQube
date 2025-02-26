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
    control_args = {}
    nested_args = {}
    custom_args = {}

    for key, value in args.items():
        if key.startswith('control_'):
            control_args[key] = value
        elif key.startswith('nested_'):
            nested_args[key] = value
        elif key.startswith('custom_'):
            custom_args[key] = value

    return control_args, nested_args