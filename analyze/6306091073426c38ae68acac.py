def dict_insert(dic, val, key, *keys):
    if not keys:
        # Base case - no more nested keys, insert value
        dic[key] = val
        return dic
    
    # Create nested dict if key doesn't exist
    if key not in dic:
        dic[key] = {}
    
    # Recursively insert into nested dictionary
    dict_insert(dic[key], val, keys[0], *keys[1:])
    return dic