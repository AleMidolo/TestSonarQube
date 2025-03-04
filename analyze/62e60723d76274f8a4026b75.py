def round_half_to_even(n):
    # Handle integer case
    if isinstance(n, int):
        return n
        
    # Get decimal part
    decimal = n - int(n)
    
    # If decimal < 0.5, round down
    if decimal < 0.5:
        return int(n)
    
    # If decimal > 0.5, round up
    elif decimal > 0.5:
        return int(n) + 1
        
    # If decimal == 0.5, round to nearest even
    else:
        if int(n) % 2 == 0:
            return int(n)
        else:
            return int(n) + 1