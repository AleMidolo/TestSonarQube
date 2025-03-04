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
                
    return silent_args