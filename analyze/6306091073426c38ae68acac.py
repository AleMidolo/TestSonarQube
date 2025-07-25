def dict_insert(dic, val, key, *keys):
    if not keys:
        dic[key] = val
        return dic
        
    if key not in dic:
        dic[key] = {}
        
    current = dic[key]
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]
        
    current[keys[-1]] = val
    return dic