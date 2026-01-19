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
    # Check rows (पंक्तियों की जांच)
    for row in range(3):
        if (self.board[row][0] == self.board[row][1] == self.board[row][2] and 
            self.board[row][0] is not None):
            return self.board[row][0]
    
    # Check columns (स्तंभों की जांच)
    for col in range(3):
        if (self.board[0][col] == self.board[1][col] == self.board[2][col] and 
            self.board[0][col] is not None):
            return self.board[0][col]
    
    # Check diagonal (top-left to bottom-right) (बाएं से दाएं तिरछी जांच)
    if (self.board[0][0] == self.board[1][1] == self.board[2][2] and 
        self.board[0][0] is not None):
        return self.board[0][0]
    
    # Check anti-diagonal (top-right to bottom-left) (दाएं से बाएं तिरछी जांच)
    if (self.board[0][2] == self.board[1][1] == self.board[2][0] and 
        self.board[0][2] is not None):
        return self.board[0][2]
    
    # No winner yet (अभी तक कोई विजेता नहीं)
    return None