def round_half_to_even(n):
    """
    Rounds a number according to round-half-to-even rules.
    For numbers exactly halfway between two integers, rounds to the nearest even number.
    For all other numbers, rounds to the nearest integer.
    """
    # If n is already an integer, return it
    if isinstance(n, int):
        return n
        
    # Get decimal part
    decimal = n - int(n)
    
    # If decimal is exactly 0.5
    if decimal == 0.5:
        # Round to nearest even number
        if int(n) % 2 == 0:  # If integer part is even
            return int(n)
        else:  # If integer part is odd
            return int(n) + 1
    
    # For all other cases, use regular rounding
    return round(n)