@staticmethod
def count_all(n: int) -> int:
    """
    Calculate the number of all possible combinations.
    :param n: The total number of elements,int.
    :return: The number of all possible combinations,int,if the number of combinations is greater than 2^63-1,return float("inf").
    >>> CombinationCalculator.count_all(4)
    15
    """
    # The total number of all possible combinations is 2^n - 1
    # (excluding the empty set)
    # For n=4: C(4,1) + C(4,2) + C(4,3) + C(4,4) = 4 + 6 + 4 + 1 = 15
    # This equals 2^4 - 1 = 16 - 1 = 15
    
    max_value = 2**63 - 1
    
    # Check if 2^n - 1 would exceed the limit
    if n >= 63:
        # 2^63 - 1 is the max, so 2^63 would already exceed it
        return float("inf")
    
    result = 2**n - 1
    
    if result > max_value:
        return float("inf")
    
    return result