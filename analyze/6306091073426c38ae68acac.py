def dict_insert(dic, val, key, *keys):
    current = dic
    for k in (key,) + keys:
        if k not in current:
            current[k] = {}
        current = current[k]
    current = val