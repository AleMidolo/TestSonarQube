def sin(self, x):
    """
    计算 x 度角的正弦值
    :param x: float
    :return: float
    >>> tricalculator.sin(30)
    0.5
    """
    import math
    return math.sin(math.radians(x))