def difference(d1, d2, level=-1):
    from copy import deepcopy

    if level == 0:
        return {}

    result = {}
    for key in d1:
        if key not in d2:
            result[key] = deepcopy(d1[key]) if isinstance(d1[key], dict) else d1[key]
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            sub_diff = difference(d1[key], d2[key], level - 1 if level > 0 else -1)
            if sub_diff:
                result[key] = sub_diff
        elif d1[key] != d2[key]:
            result[key] = deepcopy(d1[key])

    return result