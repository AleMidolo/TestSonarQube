def cos(self, x):
    """
    计算 x 度角的余弦值
    :param x: float
    :return: float
    >>> tricalculator = TriCalculator()
    >>> tricalculator.cos(60)
    0.5
    """
    # 将角度转换为弧度
    radians = math.radians(x)
    # 计算余弦值
    return math.cos(radians)