def difference(d1, d2, level=-1):
    if level == 0:
        return {}
    
    result = {}
    
    # Add items from d1 that aren't in d2
    for key in d1:
        if key not in d2:
            result[key] = d1[key]
        elif level != 1:
            # For nested dictionaries, recurse if level allows
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                nested_diff = difference(d1[key], d2[key], level - 1 if level > 0 else -1)
                if nested_diff:
                    result[key] = nested_diff
            # For non-dict values, include if they're different
            elif d1[key] != d2[key]:
                result[key] = d1[key]
        else:
            # At level 1, include if values are different
            if d1[key] != d2[key]:
                result[key] = d1[key]
                
    return result