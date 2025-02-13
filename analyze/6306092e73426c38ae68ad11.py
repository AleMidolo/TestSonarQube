def merge_extra_vars(vars_dict, extra_vars=None):
    if extra_vars is None:
        return vars_dict
    for var in extra_vars:
        if isinstance(var, dict):
            vars_dict.update(var)
    return vars_dict