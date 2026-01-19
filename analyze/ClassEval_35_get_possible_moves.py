def get_possible_moves(self, state):
    """
        अभी की स्थिति के आधार पर सभी संभावित चलने की दिशाएँ पाएँ।
        केवल चार दिशाएँ हैं: 'ऊपर', 'नीचे', 'बाएँ', 'दाएँ'।

        :param state: इंटीजर की एक 3×3 लिस्ट, जो अभी की स्थिति को स्टोर करती है
        :return moves: str की एक लिस्ट, जो अभी की स्थिति के आधार पर सभी संभावित चलने की दिशाएँ स्टोर करती है

        >>> eightPuzzle.get_possible_moves([[2, 3, 4], [5, 8, 1], [6, 0, 7]])
        ['ऊपर', 'बाएँ', 'दाएँ']
        """
    moves = []
    i, j = self.find_blank(state)
    if i > 0:
        moves.append('up')
    if i < 2:
        moves.append('down')
    if j > 0:
        moves.append('left')
    if j < 2:
        moves.append('right')
    return moves