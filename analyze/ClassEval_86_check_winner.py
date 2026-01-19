def check_winner(self):
    """
        बोर्ड पर विजेता की जांच करें, पंक्तियों, स्तंभों और तिरछी तीन दिशाओं में
        :return: str या None, विजेता का चिह्न ('X' या 'O'), या None यदि अभी तक कोई विजेता नहीं है
        >>> moves = [(1, 0), (2, 0), (1, 1), (2, 1), (1, 2)]
        >>> for move in moves:
        ...     ttt.make_move(move[0], move[1])
        >>> ttt.check_winner()
        'X'
        """
    n = len(self.board)
    for i in range(n):
        if self.board[i][0] != ' ' and all((self.board[i][j] == self.board[i][0] for j in range(n))):
            return self.board[i][0]
    for j in range(n):
        if self.board[0][j] != ' ' and all((self.board[i][j] == self.board[0][j] for i in range(n))):
            return self.board[0][j]
    if self.board[0][0] != ' ' and all((self.board[i][i] == self.board[0][0] for i in range(n))):
        return self.board[0][0]
    if self.board[0][n - 1] != ' ' and all((self.board[i][n - 1 - i] == self.board[0][n - 1] for i in range(n))):
        return self.board[0][n - 1]
    return None