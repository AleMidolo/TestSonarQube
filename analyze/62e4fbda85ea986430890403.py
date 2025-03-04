def _shuffled(seq: Sequence[str]) -> list[str]:
    """Mescolamento deterministico"""
    result = list(seq)
    for i in range(len(result)):
        j = (i * 7 + 13) % len(result)
        result[i], result[j] = result[j], result[i]
    return result