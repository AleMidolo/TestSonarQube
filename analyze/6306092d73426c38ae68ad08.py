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
        # Skip if option doesn't have required_when condition
        if 'required_when' not in option:
            continue
            
        condition = option['required_when']
        
        # Evaluate the required_when condition
        try:
            # Create context with args for condition evaluation
            context = {k: v for k, v in args.items()}
            
            # If condition evaluates to True, add argument name to required list
            if eval(condition, {"__builtins__": {}}, context):
                required_args.append(option['name'])
                
        except Exception as e:
            # Log error if condition evaluation fails
            self.logger.error(
                f"Failed to evaluate required_when condition '{condition}' "
                f"for argument '{option.get('name')}' in command '{command_name}': {str(e)}"
            )
            
    return required_args