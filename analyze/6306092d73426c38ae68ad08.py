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
            if self._evaluate_condition(condition, command_name, args):
                required_args.append(option['name'])
    
    return required_args

def _evaluate_condition(self, condition, command_name, args):
    # This is a placeholder for the actual condition evaluation logic
    # Implement the logic to evaluate the condition based on command_name and args
    return True  # Replace with actual evaluation