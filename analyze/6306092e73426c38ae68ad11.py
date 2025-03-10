def merge_extra_vars(vars_dict, extra_vars=None):
    """
    ``vars_dict`` को ``extra-vars`` के साथ मर्ज (जोड़ना) करें।

    :param vars_dict: वह डिक्शनरी जिसमें extra-vars को मर्ज करना है
    :param extra_vars: extra-vars की सूची (लिस्ट)
    """
    if extra_vars is None:
        extra_vars = []
    
    for var in extra_vars:
        key, value = var.split('=', 1)
        vars_dict[key] = value
    
    return vars_dict