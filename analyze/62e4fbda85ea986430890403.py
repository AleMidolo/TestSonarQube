from typing import Sequence
import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """Mescolamento deterministico"""
    shuffled_seq = list(seq)
    random.seed(0)  # Set a seed for deterministic shuffling
    random.shuffle(shuffled_seq)
    return shuffled_seq