def difference(d1, d2, level=-1):
    def recursive_difference(d1, d2, level):
        if level == 0:
            return {}
        result = {}
        for key in d1:
            if key not in d2:
                result[key] = d1[key]
            elif isinstance(d1[key], dict) and isinstance(d2.get(key), dict):
                nested_diff = recursive_difference(d1[key], d2[key], level - 1)
                if nested_diff:
                    result[key] = nested_diff
            elif d1[key] != d2.get(key):
                result[key] = d1[key]
        return result

    return recursive_difference(d1, d2, level)