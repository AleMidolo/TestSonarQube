def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extend ``vars_dict`` with ``extra-vars``

    :param vars_dict: Dictionary to merge extra-vars into
    :param extra_vars: List of extra-vars
    """
    if not extra_vars:
        return vars_dict
        
    if isinstance(extra_vars, list):
        for var in extra_vars:
            if isinstance(var, dict):
                vars_dict.update(var)
            elif isinstance(var, str):
                try:
                    key, value = var.split('=', 1)
                    vars_dict[key.strip()] = value.strip()
                except ValueError:
                    continue
    elif isinstance(extra_vars, dict):
        vars_dict.update(extra_vars)
        
    return vars_dict