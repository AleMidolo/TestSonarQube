def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extiende ``vars_dict`` con ``extra-vars``

    :param vars_dict: Diccionario en el que se fusionarán las extra-vars  
    :param extra_vars: Lista de extra-vars
    """
    if extra_vars is not None:
        for var in extra_vars:
            key, value = var.split('=', 1)
            vars_dict[key] = value
    return vars_dict