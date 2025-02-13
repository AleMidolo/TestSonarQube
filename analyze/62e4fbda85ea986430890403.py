from typing import Sequence
import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    random.seed(0)  # Imposta un seme per il mescolamento deterministico
    shuffled_seq = list(seq)
    random.shuffle(shuffled_seq)
    return shuffled_seq