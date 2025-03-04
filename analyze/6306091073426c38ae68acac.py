def dict_insert(dic, val, key, *keys):
    if not keys:  # If there are no more nested keys
        dic[key] = val
        return dic
    
    # Create nested dictionary if it doesn't exist
    if key not in dic:
        dic[key] = {}
    
    # Recursively insert into nested dictionaries
    dict_insert(dic[key], val, keys[0], *keys[1:])
    return dic