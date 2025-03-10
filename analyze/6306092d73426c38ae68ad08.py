def _get_conditionally_required_args(self, command_name, options_spec, args):
    """
    List arguments with ``required_when`` condition matched.

    :param command_name: the command name.
    :param options_spec:  the list of command spec options.
    :param args: the received input arguments
    :return: list, list of argument names with matched ``required_when``
        condition
    """
    required_args = []
    for option in options_spec:
        if 'required_when' in option:
            condition = option['required_when']
            if condition(command_name, args):
                required_args.append(option['name'])
    return required_args