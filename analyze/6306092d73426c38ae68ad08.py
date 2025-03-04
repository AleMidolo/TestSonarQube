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
            
        required_when = option['required_when']
        
        # Check if required_when is a callable
        if callable(required_when):
            if required_when(args):
                required_args.append(option['name'])
                
        # Check if required_when is a dict with conditions
        elif isinstance(required_when, dict):
            conditions_met = True
            
            for key, value in required_when.items():
                if key not in args or args[key] != value:
                    conditions_met = False
                    break
                    
            if conditions_met:
                required_args.append(option['name'])
                
        # Check if required_when is a string expression
        elif isinstance(required_when, str):
            try:
                if eval(required_when, {'args': args}):
                    required_args.append(option['name'])
            except:
                # Log warning that expression evaluation failed
                pass
                
    return required_args