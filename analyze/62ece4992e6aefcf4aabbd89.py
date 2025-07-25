def gaussian(x):
    """
    计算以均值 0.2 为中心，标准差为 0.1 的高斯分布。

    以均值 0.2 为中心，标准差为 0.1 的高斯分布。
    """
    import math
    
    mean = 0.2
    std = 0.1
    
    exponent = -((x - mean) ** 2) / (2 * std ** 2)
    coefficient = 1 / (std * math.sqrt(2 * math.pi))
    
    return coefficient * math.exp(exponent)