import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Barajar de manera determinista
    """
    # Convert the sequence to a list to ensure mutability
    seq_list = list(seq)
    # Use a fixed seed for deterministic shuffling
    random.seed(42)
    random.shuffle(seq_list)
    return seq_list