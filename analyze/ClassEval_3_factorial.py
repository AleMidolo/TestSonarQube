@staticmethod
def factorial(n):
    """
    दिए गए संख्या का फैक्टोरियल निकालता है।
    :param n: int, वह संख्या जिसके लिए फैक्टोरियल निकालना है।
    :return: int, दिए गए संख्या का फैक्टोरियल।
    >>> ArrangementCalculator.factorial(4)
    24

    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result