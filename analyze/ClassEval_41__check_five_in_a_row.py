def _check_five_in_a_row(self, row, col, direction):
    """
    यह जांचता है कि दिए गए सेल से शुरू होकर दिए गए दिशा (क्षैतिज, ऊर्ध्वाधर, विकर्ण) में एक ही खिलाड़ी के पांच लगातार प्रतीक हैं या नहीं।
    दिए गए सेल से शुरू होकर उस दिशा में लगातार प्रतीकों की संख्या गिनता है,
    :param row: int, दिए गए सेल की पंक्ति
    :param col: int, दिए गए सेल का कॉलम
    :param direction: tuple, (int, int), जिसे (dx, dy) के रूप में नामित किया गया है। पंक्ति और कॉलम क्रमशः कई dx और dy जोड़ेंगे।
    :return: यदि एक ही खिलाड़ी के पांच लगातार प्रतीक हैं, तो True और अन्यथा False।
    >>> gomokuGame = GomokuGame(10)
    >>> moves = [(5, 5), (0, 0), (5, 4), (0, 1), (5, 3), (0, 2), (5, 2), (0, 3), (5, 1)]
    >>> for move in moves:
    ...     gomokuGame.make_move(move[0], move[1])
    >>> gomokuGame._check_five_in_a_row(5, 1, (0, 1))
    True
    >>> gomokuGame._check_five_in_a_row(5, 1, (1, 1))
    False
    """
    # Get the player at the starting position
    player = self.board[row][col]
    
    # If the cell is empty, return False
    if player is None or player == 0 or player == '':
        return False
    
    dx, dy = direction
    count = 1  # Count the starting cell
    
    # Check in the positive direction
    current_row, current_col = row + dx, col + dy
    while (0 <= current_row < len(self.board) and 
           0 <= current_col < len(self.board[0]) and 
           self.board[current_row][current_col] == player):
        count += 1
        current_row += dx
        current_col += dy
    
    # Check in the negative direction
    current_row, current_col = row - dx, col - dy
    while (0 <= current_row < len(self.board) and 
           0 <= current_col < len(self.board[0]) and 
           self.board[current_row][current_col] == player):
        count += 1
        current_row -= dx
        current_col -= dy
    
    # Return True if we found 5 or more in a row
    return count >= 5