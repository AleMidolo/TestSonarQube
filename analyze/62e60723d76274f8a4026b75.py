def round_half_to_even(n):
    """
    Rounds a number according to round-half-to-even rules.
    For numbers exactly halfway between two integers, rounds to the nearest even number.
    For all other numbers, rounds to the nearest integer.
    
    >>> round_half_to_even(3)
    3
    >>> round_half_to_even(3.2)
    3
    >>> round_half_to_even(3.5)
    4
    >>> round_half_to_even(3.7)
    4
    >>> round_half_to_even(4)
    4
    >>> round_half_to_even(4.2)
    4
    >>> round_half_to_even(4.5)
    4
    >>> round_half_to_even(4.7)
    5
    
    :param n: Number to round
    :return: Rounded number according to round-half-to-even rules
    """
    # Get the decimal part
    decimal = abs(n - int(n))
    
    # If exactly 0.5
    if decimal == 0.5:
        # Round to nearest even number
        floor = int(n)
        if floor % 2 == 0:
            return floor
        else:
            return floor + 1
    # Otherwise use regular rounding
    else:
        return round(n)