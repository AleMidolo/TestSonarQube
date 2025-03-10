def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extend ``vars_dict`` with ``extra-vars``

    :param vars_dict: Dictionary to merge extra-vars into
    :param extra_vars: List of extra-vars
    """
    if extra_vars is None:
        extra_vars = []
    
    for var in extra_vars:
        if '=' in var:
            key, value = var.split('=', 1)
            vars_dict[key] = value
        else:
            vars_dict[var] = True
    
    return vars_dict