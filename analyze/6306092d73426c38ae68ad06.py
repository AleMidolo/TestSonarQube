def get_silent_args(self, args):
    """
    被静默的参数列表

    :param args: 接收到的参数。
    :return: list，被静默的参数名称列表。
    """
    silent_args = []
    
    # Check if args is a dictionary
    if isinstance(args, dict):
        # Iterate through args and check for silent parameters
        for arg_name, arg_value in args.items():
            # If arg value is None or empty string, consider it silent
            if arg_value is None or (isinstance(arg_value, str) and not arg_value.strip()):
                silent_args.append(arg_name)
            # If arg value is list/tuple/set and empty, consider it silent    
            elif isinstance(arg_value, (list, tuple, set)) and not arg_value:
                silent_args.append(arg_name)
            # If arg value is dict and empty, consider it silent
            elif isinstance(arg_value, dict) and not arg_value:
                silent_args.append(arg_name)
                
    return silent_args