def difference(d1, d2, level=-1):
    if level == 0:
        return {}
    
    result = {}
    
    # Handle keys in d1
    for key in d1:
        # If key not in d2, include entire subtree from d1
        if key not in d2:
            result[key] = d1[key]
        # If key in both but values differ
        elif d1[key] != d2[key]:
            # For dicts, recurse if level allows
            if isinstance(d1[key], dict) and isinstance(d2[key], dict) and level != 1:
                sub_diff = difference(d1[key], d2[key], level - 1 if level > 0 else -1)
                if sub_diff:
                    result[key] = sub_diff
            # For non-dicts or level=1, include if values differ
            elif d1[key] != d2[key]:
                result[key] = d1[key]
                
    return result