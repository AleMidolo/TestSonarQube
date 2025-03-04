def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extiende ``vars_dict`` con ``extra-vars``

    :param vars_dict: Diccionario en el que se fusionarán las extra-vars  
    :param extra_vars: Lista de extra-vars
    """
    if extra_vars is None:
        return vars_dict
        
    if isinstance(extra_vars, list):
        for extra_var in extra_vars:
            if isinstance(extra_var, dict):
                vars_dict.update(extra_var)
    elif isinstance(extra_vars, dict):
        vars_dict.update(extra_vars)
        
    return vars_dict