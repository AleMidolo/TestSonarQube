def difference(d1, d2, level=-1):
    import copy

    def recursive_difference(d1, d2, current_level):
        result = {}
        for key in d1:
            if key not in d2:
                result[key] = copy.deepcopy(d1[key])
            else:
                if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                    if current_level != 0:
                        sub_diff = recursive_difference(d1[key], d2[key], current_level - 1 if level > 0 else -1)
                        if sub_diff:
                            result[key] = sub_diff
                elif d1[key] != d2[key]:
                    result[key] = copy.deepcopy(d1[key])
        return result

    return recursive_difference(d1, d2, level)