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
        # Skip if no required_when condition
        if 'required_when' not in option:
            continue
            
        condition = option['required_when']
        
        # Evaluate the required_when condition
        try:
            # Create context with args for eval
            context = {k: v for k, v in args.items()}
            is_required = eval(condition, {"__builtins__": {}}, context)
            
            if is_required:
                required_args.append(option['name'])
                
        except Exception as e:
            # Log error and continue if condition evaluation fails
            self.logger.error(
                f"Error evaluating required_when condition for {command_name} "
                f"argument {option['name']}: {str(e)}"
            )
            continue
            
    return required_args