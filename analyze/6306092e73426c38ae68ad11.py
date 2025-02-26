def merge_extra_vars(vars_dict, extra_vars=None):
    """
    ``vars_dict`` को ``extra-vars`` के साथ मर्ज (जोड़ना) करें।

    :param vars_dict: वह डिक्शनरी जिसमें extra-vars को मर्ज करना है
    :param extra_vars: extra-vars की सूची (लिस्ट)
    """
    if extra_vars is None:
        return vars_dict
    
    for var in extra_vars:
        if isinstance(var, dict):
            vars_dict.update(var)
        else:
            raise ValueError("Each item in extra_vars must be a dictionary.")
    
    return vars_dict