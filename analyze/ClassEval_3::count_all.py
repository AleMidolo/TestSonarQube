@staticmethod
def count_all(n):
    """
        Conta il numero totale di tutti i possibili arrangiamenti scegliendo almeno 1 elemento e al massimo n elementi da n elementi.
        :param n: int, il numero totale di elementi.
        :return: int, il conteggio di tutti gli arrangiamenti.
        >>> ArrangementCalculator.count_all(4)
        64

        """
    total = 0
    for m in range(1, n + 1):
        total += ArrangementCalculator.factorial(n) // ArrangementCalculator.factorial(n - m)
    return total