def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    निर्धारित (Deterministically) तरीके से शफल करें
    """
    # Convert sequence to list for shuffling
    result = list(seq)
    
    # Use deterministic Fisher-Yates shuffle
    for i in range(len(result)-1, 0, -1):
        # Use deterministic index based on position
        j = (i * 1337) % (i + 1)
        # Swap elements
        result[i], result[j] = result[j], result[i]
        
    return result