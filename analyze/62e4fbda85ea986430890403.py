import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Barajar de manera determinista
    """
    # Use a fixed seed for deterministic shuffling
    random.seed(42)
    shuffled_seq = seq.copy()
    random.shuffle(shuffled_seq)
    return shuffled_seq