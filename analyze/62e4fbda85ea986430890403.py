import random
from typing import Sequence

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    Barajar de manera determinista
    """
    random.seed(0)  # Set a seed for reproducibility
    shuffled_seq = list(seq)
    random.shuffle(shuffled_seq)
    return shuffled_seq