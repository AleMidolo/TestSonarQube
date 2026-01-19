def count(n, m=None):
    """
    n आइटम में से m आइटम चुनकर व्यवस्थाओं की संख्या गिनता है (परम्यूटेशन)।
    यदि m प्रदान नहीं किया गया है या n, m के बराबर है, तो factorial(n) लौटाता है।
    :param n: int, आइटम की कुल संख्या।
    :param m: int, चुने जाने वाले आइटम की संख्या (डिफ़ॉल्ट=None)।
    :return: int, व्यवस्थाओं की संख्या।
    >>> ArrangementCalculator.count(5, 3)
    60

    """
    import math
    
    if m is None or m == n:
        return math.factorial(n)
    
    # P(n, m) = n! / (n - m)!
    return math.factorial(n) // math.factorial(n - m)