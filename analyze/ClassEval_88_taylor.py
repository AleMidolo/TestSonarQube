def taylor(self, x, n):
    """
    计算 cos (x/180 * pi) 的 n 阶泰勒展开值
    :param x: int
    :param n: int
    :return: float
    >>> tricalculator.taylor(60, 50)
    0.5000000000000001
    """
    # 将角度转换为弧度
    rad = x / 180 * math.pi

    # cos(x) 的泰勒展开式: cos(x) = Σ((-1)^k * x^(2k) / (2k)!) for k=0 to n
    result = 0.0

    for k in range(n + 1):
        # 计算第 k 项: (-1)^k * rad^(2k) / (2k)!
        term = ((-1) ** k) * (rad ** (2 * k)) / math.factorial(2 * k)
        result += term

    return result