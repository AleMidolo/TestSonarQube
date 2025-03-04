def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle
    """
    # Convert sequence to list to make it mutable
    result = list(seq)
    
    # Use a fixed seed for deterministic shuffling
    n = len(result)
    for i in range(n-1):
        # Use a deterministic formula to swap elements
        j = (i * i + n) % n
        result[i], result[j] = result[j], result[i]
        
    return result