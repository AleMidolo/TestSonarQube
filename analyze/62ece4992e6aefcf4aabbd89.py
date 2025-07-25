import numpy as np

def gaussian(x):
    """
    计算以均值 0.2 为中心，标准差为 0.1 的高斯分布。

    以均值 0.2 为中心，标准差为 0.1 的高斯分布。
    """
    mean = 0.2
    std_dev = 0.1
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)