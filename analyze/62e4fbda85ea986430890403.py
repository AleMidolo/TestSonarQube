def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle
    """
    # Convert sequence to list to make it mutable
    result = list(seq)
    
    # Use deterministic shuffle by iterating through indices
    for i in range(len(result)-1, 0, -1):
        # Use a deterministic formula to pick swap index
        j = (i * 1337 + 7) % (i + 1)
        # Swap elements
        result[i], result[j] = result[j], result[i]
        
    return result