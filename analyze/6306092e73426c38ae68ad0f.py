def get_nested_custom_and_control_args(self, args):
    control_args = {}
    nested_args = {}
    
    for key, value in args.items():
        if key.startswith('control_'):
            control_args[key] = value
        elif key.startswith('nested_'):
            nested_args[key] = value
        else:
            control_args[key] = value  # Assuming custom args are treated as control args

    return control_args, nested_args