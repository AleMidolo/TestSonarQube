def gaussian(x):
    """
    计算以均值 0.2 为中心，标准差为 0.1 的高斯分布。

    以均值 0.2 为中心，标准差为 0.1 的高斯分布。
    """
    import math
    mean = 0.2
    std_dev = 0.1
    coefficient = 1 / (std_dev * math.sqrt(2 * math.pi))
    exponent = math.exp(-0.5 * ((x - mean) / std_dev) ** 2)
    return coefficient * exponent