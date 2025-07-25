def _replace_register(flow_params, register_number, register_value):
    """
    Replace value from flows to given register number

    'register_value' key in dictionary will be replaced by register number
    given by 'register_number'

    :param flow_params: Dictionary containing defined flows
    :param register_number: The number of register where value will be stored
    :param register_value: Key to be replaced by register number
    """
    # Handle nested dictionaries recursively
    if isinstance(flow_params, dict):
        for key, value in flow_params.items():
            if key == register_value:
                flow_params[key] = register_number
            elif isinstance(value, (dict, list)):
                _replace_register(value, register_number, register_value)
                
    # Handle lists recursively
    elif isinstance(flow_params, list):
        for i, item in enumerate(flow_params):
            if isinstance(item, (dict, list)):
                _replace_register(item, register_number, register_value)
            elif item == register_value:
                flow_params[i] = register_number
                
    return flow_params