def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Estende ``vars_dict`` con ``extra-vars``

    :param vars_dict: Dizionario in cui unire le extra-vars
    :param extra_vars: Lista di extra-vars
    """
    if extra_vars is None:
        return vars_dict
    
    for var in extra_vars:
        if isinstance(var, dict):
            vars_dict.update(var)
        else:
            raise ValueError("Each extra-var must be a dictionary.")
    
    return vars_dict