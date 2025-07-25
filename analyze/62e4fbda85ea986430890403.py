import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle the input sequence of strings.
    """
    # Create a copy of the sequence to avoid modifying the original
    seq_copy = list(seq)
    
    # Use a fixed seed for deterministic shuffling
    random.seed(42)
    
    # Shuffle the sequence
    random.shuffle(seq_copy)
    
    return seq_copy