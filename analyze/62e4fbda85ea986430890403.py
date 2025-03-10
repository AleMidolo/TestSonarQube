import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle the input sequence of strings.
    """
    # Create a copy of the sequence to avoid modifying the original
    seq_copy = list(seq)
    # Seed the random number generator for deterministic behavior
    random.seed(42)
    # Shuffle the sequence in place
    random.shuffle(seq_copy)
    return seq_copy