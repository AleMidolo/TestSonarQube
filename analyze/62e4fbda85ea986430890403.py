from typing import Sequence
import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    निर्धारित (Deterministically) तरीके से शफल करें
    """
    random.seed(0)  # Set a seed for reproducibility
    shuffled_seq = list(seq)
    random.shuffle(shuffled_seq)
    return shuffled_seq