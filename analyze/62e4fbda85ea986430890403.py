import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    निर्धारित (Deterministically) तरीके से शफल करें
    """
    # Use a fixed seed for deterministic shuffling
    random.seed(42)
    shuffled_seq = list(seq)
    random.shuffle(shuffled_seq)
    return shuffled_seq