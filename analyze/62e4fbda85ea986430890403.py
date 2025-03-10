import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """Mescolamento deterministico"""
    # Create a copy of the sequence to avoid modifying the original
    seq_copy = list(seq)
    # Seed the random number generator with a fixed value to ensure determinism
    random.seed(42)
    # Shuffle the copy
    random.shuffle(seq_copy)
    return seq_copy