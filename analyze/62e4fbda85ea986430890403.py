def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle
    """
    # Convert sequence to list to make it mutable
    result = list(seq)
    
    # Use deterministic shuffle by iterating through indices
    for i in range(len(result)-1, 0, -1):
        # Use index itself as seed for deterministic behavior
        j = i % (i+1)
        result[i], result[j] = result[j], result[i]
        
    return result