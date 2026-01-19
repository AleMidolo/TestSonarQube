@staticmethod
def count_all(n: int) -> int:
    """
    计算所有可能组合的数量。
    :param n: 元素的总数，int。
    :return: 所有可能组合的数量，int。如果组合数量大于 2^63-1，则返回 float("inf")。
    >>> CombinationCalculator.count_all(4)
    15
    """
    # 所有可能的组合数量是 2^n - 1 (排除空集)
    # C(n,0) + C(n,1) + C(n,2) + ... + C(n,n) = 2^n
    # 减去空集 C(n,0) = 1，得到 2^n - 1
    
    max_value = 2**63 - 1
    
    # 检查 2^n - 1 是否超过 2^63 - 1
    if n >= 63:
        # 当 n >= 63 时，2^n - 1 >= 2^63 - 1
        # 实际上当 n > 63 时，2^n - 1 > 2^63 - 1
        if n > 63:
            return float("inf")
        # 当 n == 63 时，2^63 - 1 正好等于 max_value
        else:
            return max_value
    
    result = (1 << n) - 1  # 2^n - 1
    return result