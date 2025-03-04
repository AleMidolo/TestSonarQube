def get_silent_args(self, args):
    """
    list of silenced argument

    :param args: The received arguments.
    :return: list, slienced argument names
    """
    silent_args = []
    
    # Check if args is a dictionary
    if isinstance(args, dict):
        # Look for arguments that have None or empty values
        for arg_name, arg_value in args.items():
            if arg_value is None or arg_value == '':
                silent_args.append(arg_name)
                
    # If args is a list/tuple, check each element
    elif isinstance(args, (list, tuple)):
        for i, arg in enumerate(args):
            if arg is None or arg == '':
                silent_args.append(i)
                
    return silent_args