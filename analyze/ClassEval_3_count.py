@staticmethod
def count(n, m=None):
    """
        Conta il numero di disposizioni scegliendo m elementi da n elementi (permutazioni).
        Se m non è fornito o n è uguale a m, restituisce factorial(n).
        :param n: int, il numero totale di elementi.
        :param m: int, il numero di elementi da scegliere (default=None).
        :return: int, il conteggio delle disposizioni.
        >>> ArrangementCalculator.count(5, 3)
        60

        """
    if m is None or n == m:
        return ArrangementCalculator.factorial(n)
    return ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)