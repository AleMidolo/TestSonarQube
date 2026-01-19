def tan(self, x):
    """
    计算 x 度角的正切值
    :param x: 浮点数
    :return: 浮点数
    >>> tricalculator.tan(45)
    1.0
    """
    import math
    return math.tan(math.radians(x))