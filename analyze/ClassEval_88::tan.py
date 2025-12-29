def tan(self, x):
    """
        计算 x 度角的正切值
        :param x: 浮点数
        :return: 浮点数
        >>> tricalculator.tan(45)
        1.0
        """
    sin_val = self.sin(x)
    cos_val = self.cos(x)
    if fabs(cos_val) < 1e-10:
        raise ValueError('Tangent is undefined for angles where cosine is zero')
    return round(sin_val / cos_val, 10)