def dict_insert(dic, val, key, *keys):
    """
    Insert a value of a nested key into a dictionary.

    To insert a value for a nested key, all ancestor keys should be given as
    method's arguments.

    Example:
      dict_insert({}, 'val', 'key1.key2'.split('.'))

    :param dic: a dictionary object to insert the nested key value into
    :param val: a value to insert to the given dictionary
    :param key: first key in a chain of keys that will store the value
    :param keys: sub keys in the keys chain
    """
    current = dic
    for k in keys[:-1]:
        if k not in current:
            current[k] = {}
        current = current[k]
    current[keys[-1] if keys else key] = val