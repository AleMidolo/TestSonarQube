def merge_extra_vars(vars_dict, extra_vars=None):
    """
    使用 ``extra-vars`` 扩展 ``vars_dict``。

    :param vars_dict: 要合并 extra-vars 的字典
    :param extra_vars: extra-vars的列表
    """
    if extra_vars is None:
        return vars_dict
    
    for var in extra_vars:
        if isinstance(var, dict):
            vars_dict.update(var)
        else:
            key, value = var.split('=', 1)
            vars_dict[key] = value
            
    return vars_dict