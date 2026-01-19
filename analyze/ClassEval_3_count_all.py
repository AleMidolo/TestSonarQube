@staticmethod
def count_all(n):
    """
    सभी संभावित व्यवस्थाओं की कुल संख्या की गणना करता है, जिसमें कम से कम 1 आइटम और अधिकतम n आइटम n आइटम से चुने जाते हैं।
    :param n: int, आइटम की कुल संख्या।
    :return: int, सभी व्यवस्थाओं की संख्या।
    >>> ArrangementCalculator.count_all(4)
    64

    """
    import math
    
    total = 0
    for k in range(1, n + 1):
        # P(n, k) = n! / (n - k)!
        total += math.perm(n, k)
    
    return total