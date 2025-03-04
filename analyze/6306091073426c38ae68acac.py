def dict_insert(dic, val, key, *keys):
    if not keys:  # If there are no more nested keys
        dic[key] = val
        return dic
    
    # Create nested dictionary if it doesn't exist
    if key not in dic:
        dic[key] = {}
    
    # Recursively insert into nested dictionaries
    current_dict = dic[key]
    next_key = keys[0]
    remaining_keys = keys[1:]
    
    return dict_insert(current_dict, val, next_key, *remaining_keys)