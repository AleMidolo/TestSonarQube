def round_half_to_even(n):
    """
    Rounds a number to the nearest integer, with ties (i.e., 0.5) rounded to the nearest even integer.

    :param n: The number to round.
    :return: The rounded integer.
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