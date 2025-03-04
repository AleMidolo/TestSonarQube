def _shuffled(seq: Sequence[str]) -> list[str]:
    """
    使用给定的固定随机种子（FIXED_RANDOM_SEED）对给定的序列进行洗牌
    """
    import random
    FIXED_RANDOM_SEED = 42
    
    # Convert sequence to list for shuffling
    result = list(seq)
    
    # Set random seed
    random.seed(FIXED_RANDOM_SEED)
    
    # Shuffle the list
    random.shuffle(result)
    
    return result