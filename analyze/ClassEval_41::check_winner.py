def check_winner(self):
    """
        यह जांचता है कि क्या कोई विजेता है, सभी दिशाओं (क्षैतिज, ऊर्ध्वाधर, तिरछा) में पांच लगातार देखने के लिए।
        लौटाता है: विजेता खिलाड़ी का प्रतीक (या तो 'X' या 'O') यदि कोई विजेता है, अन्यथा None।
        >>> gomokuGame = GomokuGame(10)
        >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
        >>> for move in moves:
        ...     gomokuGame.make_move(move[0], move[1])
        >>> gomokuGame.check_winner()
        'X'
        """
    for row in range(self.board_size):
        for col in range(self.board_size):
            if self.board[row][col] != ' ':
                current_symbol = self.board[row][col]
                directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
                for direction in directions:
                    if self._check_five_in_a_row(row, col, direction):
                        return current_symbol
    return None