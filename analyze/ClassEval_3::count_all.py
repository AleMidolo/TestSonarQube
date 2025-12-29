@staticmethod
def count_all(n):
    """
        Counts the total number of all possible arrangements by choosing at least 1 item and at most n items from n items.
        :param n: int, the total number of items.
        :return: int, the count of all arrangements.
        >>> ArrangementCalculator.count_all(4)
        64

        """
    total = 0
    for i in range(1, n + 1):
        total += ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - i)
    return total