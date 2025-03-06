def round_half_to_even(n):
    """
    Rounds a number to the nearest integer, with ties (i.e., 0.5) rounded to the nearest even integer.

    Args:
        n (float or int): The number to round.

    Returns:
        int: The rounded integer.
    """
    if n % 1 == 0.5:
        # If the fractional part is exactly 0.5, round to the nearest even integer
        if int(n) % 2 == 0:
            return int(n)
        else:
            return int(n) + 1
    else:
        # Otherwise, round to the nearest integer
        return round(n)