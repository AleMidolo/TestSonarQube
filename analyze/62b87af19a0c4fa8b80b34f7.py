def difference(d1, d2, level=-1):
    def recursive_difference(dict1, dict2, current_level):
        result = {}
        for key in dict1:
            if key not in dict2:
                result[key] = dict1[key]
            else:
                if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                    if current_level != 0:
                        nested_diff = recursive_difference(dict1[key], dict2[key], current_level - 1)
                        if nested_diff:
                            result[key] = nested_diff
                elif dict1[key] != dict2[key]:
                    result[key] = dict1[key]
        return result

    return recursive_difference(d1, d2, level)