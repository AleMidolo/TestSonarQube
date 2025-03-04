def difference(d1, d2, level=-1):
    """
    Returns a dictionary containing items from d1 that are not in d2.
    
    Args:
        d1: First dictionary
        d2: Second dictionary 
        level: Maximum recursion depth. Set to -1 for infinite recursion.
        
    Returns:
        Dictionary containing items from d1 that are not in d2
    """
    result = {}
    
    # Handle base case where level is 0
    if level == 0:
        return d1.copy()
        
    for key in d1:
        # If key not in d2, include it in result
        if key not in d2:
            result[key] = d1[key]
            
        # If key in both d1 and d2
        elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
            # Recurse if both values are dictionaries and level allows
            if level != 1:
                diff = difference(d1[key], d2[key], level-1 if level > 0 else -1)
                if diff:
                    result[key] = diff
                    
        # If values are different, include in result for level 1+
        elif d1[key] != d2[key]:
            result[key] = d1[key]
            
    return result