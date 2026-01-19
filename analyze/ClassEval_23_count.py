def count(n: int, m: int) -> int:
    """
    किसी तय गिनती के लिए कॉम्बिनेशन की संख्या कैलकुलेट करें।

    :param n: एलिमेंट की कुल संख्या, int
    :param m: हर कॉम्बिनेशन में एलिमेंट की संख्या, int
    :return: कॉम्बिनेशन की संख्या, int

    >>> CombinationCalculator.count(4, 2)
    6
    """
    # Handle edge cases
    if m > n or m < 0 or n < 0:
        return 0
    if m == 0 or m == n:
        return 1
    
    # Calculate factorial helper
    def factorial(num):
        if num <= 1:
            return 1
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
    
    # Combination formula: C(n, m) = n! / (m! * (n - m)!)
    # Optimize by using the smaller factorial in denominator
    m = min(m, n - m)
    
    # Calculate using the optimized formula
    numerator = 1
    denominator = 1
    
    for i in range(m):
        numerator *= (n - i)
        denominator *= (i + 1)
    
    return numerator // denominator