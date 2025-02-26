def difference(d1, d2, level=-1):
    from collections.abc import MutableMapping
    import copy

    if level == 0:
        return {}

    result = {}
    for key in d1:
        if key not in d2:
            result[key] = copy.deepcopy(d1[key]) if level != 0 else d1[key]
        else:
            if isinstance(d1[key], MutableMapping) and isinstance(d2[key], MutableMapping):
                sub_diff = difference(d1[key], d2[key], level - 1)
                if sub_diff:
                    result[key] = sub_diff
            elif d1[key] != d2[key]:
                result[key] = copy.deepcopy(d1[key]) if level != 0 else d1[key]

    return result