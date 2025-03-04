def merge_extra_vars(vars_dict, extra_vars=None):
    """
    使用 ``extra-vars`` 扩展 ``vars_dict``。

    :param vars_dict: 要合并 extra-vars 的字典
    :param extra_vars: extra-vars的列表
    """
    if not extra_vars:
        return vars_dict
        
    if isinstance(extra_vars, str):
        extra_vars = [extra_vars]
        
    for extra_var in extra_vars:
        if '=' not in extra_var:
            continue
            
        key, value = extra_var.split('=', 1)
        key = key.strip()
        value = value.strip()
        
        # Try to convert string value to Python type
        try:
            # Handle boolean values
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            # Handle numeric values    
            elif value.isdigit():
                value = int(value)
            elif value.replace('.','',1).isdigit():
                value = float(value)
        except:
            pass
            
        vars_dict[key] = value
        
    return vars_dict