def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extend ``vars_dict`` with ``extra-vars``

    :param vars_dict: Dictionary to merge extra-vars into
    :param extra_vars: List of extra-vars
    """
    if extra_vars is None:
        return vars_dict
    
    for var in extra_vars:
        if isinstance(var, dict):
            vars_dict.update(var)
        elif isinstance(var, str):
            key_value = var.split('=', 1)
            if len(key_value) == 2:
                vars_dict[key_value[0]] = key_value[1]
    
    return vars_dict