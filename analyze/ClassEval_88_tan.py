import math

def tan(self, x):
    """
    计算 x 度角的正切值
    :param x: 浮点数
    :return: 浮点数
    >>> tricalculator.tan(45)
    1.0
    """
    # 将角度转换为弧度
    radians = math.radians(x)
    # 计算正切值
    return math.tan(radians)