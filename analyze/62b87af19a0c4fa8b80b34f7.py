def difference(d1, d2, level=-1):
    import copy

    def recursive_difference(d1, d2, current_level):
        result = {}
        for key in d1:
            if key not in d2:
                result[key] = copy.deepcopy(d1[key])
            else:
                if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                    if level == -1 or current_level < level:
                        nested_diff = recursive_difference(d1[key], d2[key], current_level + 1)
                        if nested_diff:
                            result[key] = nested_diff
                elif d1[key] != d2[key]:
                    result[key] = copy.deepcopy(d1[key])
        return result

    return recursive_difference(d1, d2, 0)