def round_half_to_even(n):
    """
    Rounds a number to the nearest integer, with ties (i.e., 0.5) rounded to the nearest even integer.

    Esempi di utilizzo della funzione:

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
    """
    integer_part = int(n)
    fractional_part = n - integer_part
    
    if fractional_part < 0.5:
        return integer_part
    elif fractional_part > 0.5:
        return integer_part + 1
    else:
        # If the fractional part is exactly 0.5, round to the nearest even integer
        if integer_part % 2 == 0:
            return integer_part
        else:
            return integer_part + 1