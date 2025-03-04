def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Barajar de manera determinista
    """
    result = list(seq)
    n = len(result)
    for i in range(n-1, 0, -1):
        j = (i * 31) % (i + 1)  # Deterministic shuffle using fixed multiplier
        result[i], result[j] = result[j], result[i]
    return result