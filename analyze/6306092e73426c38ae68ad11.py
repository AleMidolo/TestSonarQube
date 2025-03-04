def merge_extra_vars(vars_dict, extra_vars=None):
    """
    Extend ``vars_dict`` with ``extra-vars``

    :param vars_dict: Dictionary to merge extra-vars into
    :param extra_vars: List of extra-vars
    """
    if not extra_vars:
        return vars_dict
        
    for var in extra_vars:
        if '=' not in var:
            continue
            
        key, value = var.split('=', 1)
        key = key.strip()
        value = value.strip()
        
        # Try to convert value to appropriate type
        try:
            # Try to convert to int
            value = int(value)
        except ValueError:
            try:
                # Try to convert to float
                value = float(value)
            except ValueError:
                # Handle boolean values
                if value.lower() == 'true':
                    value = True
                elif value.lower() == 'false':
                    value = False
                # Otherwise keep as string
                
        vars_dict[key] = value
        
    return vars_dict