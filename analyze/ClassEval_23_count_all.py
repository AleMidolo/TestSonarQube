@staticmethod
def count_all(n: int) -> int:
    """
        सभी संभावित संयोजनों की संख्या की गणना करें।
        :param n: तत्वों की कुल संख्या, int.
        :return: सभी संभावित संयोजनों की संख्या, int, यदि संयोजनों की संख्या 2^63-1 से अधिक है, तो float("inf") लौटाएं।
        >>> CombinationCalculator.count_all(4)
        15
        """
    total_combinations = (1 << n) - 1
    return total_combinations if total_combinations <= 2 ** 63 - 1 else float('inf')