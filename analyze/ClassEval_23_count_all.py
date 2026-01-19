@staticmethod
def count_all(n: int) -> int:
    """
    Calcola il numero di tutte le possibili combinazioni.
    :param n: Il numero totale di elementi, int.
    :return: Il numero di tutte le possibili combinazioni, int; se il numero di combinazioni è maggiore di 2^63-1, restituisce float("inf").
    >>> CombinationCalculator.count_all(4)
    15
    """
    # Il numero totale di combinazioni è 2^n - 1 (escludendo l'insieme vuoto)
    # Per n=4: C(4,1) + C(4,2) + C(4,3) + C(4,4) = 4 + 6 + 4 + 1 = 15
    # Che equivale a 2^4 - 1 = 16 - 1 = 15
    
    max_value = 2**63 - 1
    
    # Calcola 2^n - 1
    total_combinations = 2**n - 1
    
    # Verifica se supera il limite
    if total_combinations > max_value:
        return float("inf")
    
    return total_combinations