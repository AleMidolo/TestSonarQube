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
    # Define all four directions to check: horizontal, vertical, and two diagonals
    directions = [
        (0, 1),   # Horizontal (right)
        (1, 0),   # Vertical (down)
        (1, 1),   # Diagonal (down-right)
        (1, -1)   # Diagonal (down-left)
    ]
    
    # Iterate through each cell on the board
    for row in range(self.board_size):
        for col in range(self.board_size):
            # Skip empty cells
            if self.board[row][col] is None:
                continue
            
            player = self.board[row][col]
            
            # Check each direction
            for dr, dc in directions:
                count = 1  # Count the current cell
                
                # Check in the positive direction
                r, c = row + dr, col + dc
                while (0 <= r < self.board_size and 
                       0 <= c < self.board_size and 
                       self.board[r][c] == player):
                    count += 1
                    r += dr
                    c += dc
                
                # Check in the negative direction
                r, c = row - dr, col - dc
                while (0 <= r < self.board_size and 
                       0 <= c < self.board_size and 
                       self.board[r][c] == player):
                    count += 1
                    r -= dr
                    c -= dc
                
                # If we found 5 or more in a row, we have a winner
                if count >= 5:
                    return player
    
    return None