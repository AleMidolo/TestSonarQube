import random

def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    使用给定的固定随机种子（FIXED_RANDOM_SEED）对给定的序列进行洗牌
    """
    FIXED_RANDOM_SEED = 42  # 固定随机种子
    random.seed(FIXED_RANDOM_SEED)
    shuffled_seq = seq.copy()
    random.shuffle(shuffled_seq)
    return shuffled_seq