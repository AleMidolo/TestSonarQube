def merge_extra_vars(vars_dict, extra_vars=None):
    """
    ``vars_dict`` को ``extra-vars`` के साथ मर्ज (जोड़ना) करें।

    :param vars_dict: वह डिक्शनरी जिसमें extra-vars को मर्ज करना है 
    :param extra_vars: extra-vars की सूची (लिस्ट)
    """
    if not extra_vars:
        return vars_dict
        
    if isinstance(extra_vars, list):
        for item in extra_vars:
            if isinstance(item, dict):
                vars_dict.update(item)
    elif isinstance(extra_vars, dict):
        vars_dict.update(extra_vars)
        
    return vars_dict