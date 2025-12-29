@staticmethod
def count_all(n: int) -> int:
    """
        सभी संभावित संयोजनों की संख्या की गणना करें।
        :param n: तत्वों की कुल संख्या, int.
        :return: सभी संभावित संयोजनों की संख्या, int, यदि संयोजनों की संख्या 2^63-1 से अधिक है, तो float("inf") लौटाएं।
        >>> CombinationCalculator.count_all(4)
        15
        """
    total = 0
    max_int = (1 << 63) - 1
    for m in range(1, n + 1):
        comb_count = CombinationCalculator.count(n, m)
        if total > max_int - comb_count:
            return float('inf')
        total += comb_count
    return total