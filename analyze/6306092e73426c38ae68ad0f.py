def get_nested_custom_and_control_args(self, args):
    control_args = {}
    nested_args = {}
    
    for key, value in args.items():
        if isinstance(value, dict):
            nested_args[key] = value
        else:
            control_args[key] = value
            
    return control_args, nested_args