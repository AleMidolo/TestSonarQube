import random
from typing import Sequence

FIXED_RANDOM_SEED = 42  # 固定随机种子

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    使用给定的固定随机种子（FIXED_RANDOM_SEED）对给定的序列进行洗牌
    """
    random.seed(FIXED_RANDOM_SEED)
    shuffled_seq = list(seq)
    random.shuffle(shuffled_seq)
    return shuffled_seq