def difference(d1, d2, level=-1):
    def recursive_diff(d1, d2, level):
        if level == 0:
            return {}
        diff = {}
        for key in d1:
            if key not in d2:
                diff[key] = d1[key]
            else:
                if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                    nested_diff = recursive_diff(d1[key], d2[key], level - 1)
                    if nested_diff:
                        diff[key] = nested_diff
                elif d1[key] != d2[key]:
                    diff[key] = d1[key]
        return diff

    return recursive_diff(d1, d2, level)