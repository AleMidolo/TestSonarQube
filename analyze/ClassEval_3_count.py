@staticmethod
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
    if m is None or n == m:
        return ArrangementCalculator.factorial(n)
    if m > n:
        return 0
    result = 1
    for i in range(n, n - m, -1):
        result *= i
    return result