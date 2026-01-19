def select_all(self):
    """
        सभी व्यवस्थाओं की एक सूची उत्पन्न करता है, जिसमें कम से कम 1 आइटम और अधिकतम आंतरिक डेटा की संख्या का चयन किया जाता है।
        :return: सूची, सभी व्यवस्थाओं की एक सूची।
        >>> ac = ArrangementCalculator([1, 2, 3])
        >>> ac.select_all()
        [[1], [2], [3], [1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2], [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

        """
    result = []
    n = len(self.datas)
    for i in range(1, n + 1):
        for permutation in itertools.permutations(self.datas, i):
            result.append(list(permutation))
    return result