def round_half_to_even(n):
    """
    Rounds a number to the nearest integer, with ties (i.e., 0.5) rounded to the nearest even integer.

    Args:
        n (float or int): The number to round.

    Returns:
        int: The rounded integer.
    """
    if n % 1 == 0.5:
        if int(n) % 2 == 0:
            return int(n)
        else:
            return int(n) + 1
    else:
        return round(n)