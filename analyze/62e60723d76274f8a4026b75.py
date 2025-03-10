def round_half_to_even(n):
    """
    将浮点数进行四舍五入到最接近的偶数
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

    :param n: 浮点数
    :return: 四舍五入到最接近的偶数
    """
    if n % 1 == 0.5:
        if int(n) % 2 == 0:
            return int(n)
        else:
            return int(n) + 1
    else:
        return round(n)