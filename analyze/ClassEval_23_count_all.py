@staticmethod
def count_all(n: int) -> int:
    """
    सभी संभावित संयोजनों की संख्या की गणना करें।
    :param n: तत्वों की कुल संख्या, int.
    :return: सभी संभावित संयोजनों की संख्या, int, यदि संयोजनों की संख्या 2^63-1 से अधिक है, तो float("inf") लौटाएं।
    >>> CombinationCalculator.count_all(4)
    15
    """
    # Total combinations = C(n,0) + C(n,1) + C(n,2) + ... + C(n,n) = 2^n - 1
    # (excluding the empty set)
    
    # Check if 2^n - 1 exceeds 2^63 - 1
    max_value = 2**63 - 1
    
    # If n >= 63, then 2^n - 1 >= 2^63 - 1
    if n >= 63:
        # Check if 2^n - 1 > 2^63 - 1
        if n > 63:
            return float("inf")
        else:  # n == 63
            # 2^63 - 1 == 2^63 - 1, so it's equal, not greater
            return 2**n - 1
    
    return 2**n - 1