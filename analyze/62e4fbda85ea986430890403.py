import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Deterministically shuffle the input sequence of strings.
    The shuffle is deterministic because the random seed is fixed.
    """
    random.seed(42)  # Fixed seed for deterministic shuffling
    shuffled_seq = list(seq)  # Create a mutable copy of the sequence
    random.shuffle(shuffled_seq)  # Shuffle the sequence in-place
    return shuffled_seq