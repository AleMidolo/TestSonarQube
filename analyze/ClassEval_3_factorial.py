@staticmethod
def factorial(n):
    """
        दिए गए संख्या का फैक्टोरियल निकालता है।
        :param n: int, वह संख्या जिसके लिए फैक्टोरियल निकालना है।
        :return: int, दिए गए संख्या का फैक्टोरियल।
        >>> ArrangementCalculator.factorial(4)
        24
        """
    if n == 0 or n == 1:
        return 1
    else:
        return n * ArrangementCalculator.factorial(n - 1)