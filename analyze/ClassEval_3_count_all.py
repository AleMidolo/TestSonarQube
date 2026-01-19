@staticmethod
def count_all(n):
    """
    Conta il numero totale di tutti i possibili arrangiamenti scegliendo almeno 1 elemento e al massimo n elementi da n elementi.
    :param n: int, il numero totale di elementi.
    :return: int, il conteggio di tutti gli arrangiamenti.
    >>> ArrangementCalculator.count_all(4)
    64

    """
    import math
    
    total = 0
    for k in range(1, n + 1):
        # P(n, k) = n! / (n-k)!
        total += math.factorial(n) // math.factorial(n - k)
    
    return total