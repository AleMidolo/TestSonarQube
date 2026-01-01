def find_blank(self, state):
    """
        वर्तमान स्थिति का खाली स्थान खोजें, जो 0 तत्व है।
        :param state: एक 3*3 आकार की सूची Integer की, जो वर्तमान स्थिति को संग्रहीत करती है।
        :return i, j: दो Integers, जो खाली ब्लॉक के निर्देशांक का प्रतिनिधित्व करते हैं।
        >>> eightPuzzle = EightPuzzle([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        >>> eightPuzzle.find_blank([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        (2, 1)
        """
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return (i, j)
    return None