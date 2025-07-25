def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Estende ``vars_dict`` con ``extra-vars``

    :param vars_dict: Dizionario in cui unire le extra-vars
    :param extra_vars: Lista di extra-vars
    """
    if extra_vars is not None:
        for var in extra_vars:
            if '=' in var:
                key, value = var.split('=', 1)
                vars_dict[key] = value
    return vars_dict