def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extiende ``vars_dict`` con ``extra-vars``

    :param vars_dict: Diccionario en el que se fusionarán las extra-vars  
    :param extra_vars: Lista de extra-vars
    """
    if extra_vars is None:
        return vars_dict
    
    for var in extra_vars:
        if '=' in var:
            key, value = var.split('=', 1)
            vars_dict[key] = value
        else:
            vars_dict[var] = None
    
    return vars_dict