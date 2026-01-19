def cos(self, x):
    """
    计算 x 度角的余弦值
    :param x: float
    :return: float
    >>> tricalculator = TriCalculator()
    >>> tricalculator.cos(60)
    0.5
    """
    import math
    return math.cos(math.radians(x))