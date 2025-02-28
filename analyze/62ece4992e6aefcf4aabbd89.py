import math

def gaussian(x):
    """
    计算以均值 0.2 为中心，标准差为 0.1 的高斯分布。

    参数:
    x (float): 输入值

    返回:
    float: 高斯分布的值
    """
    mean = 0.2
    std_dev = 0.1
    exponent = -((x - mean) ** 2) / (2 * (std_dev ** 2))
    coefficient = 1 / (std_dev * math.sqrt(2 * math.pi))
    return coefficient * math.exp(exponent)