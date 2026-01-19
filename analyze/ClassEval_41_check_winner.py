def check_winner(self):
    """
    Checks if there is a winner by looking for five in a row in all directions (horizontal, vertical, diagonal).
    return: the symbol of the winning player (either 'X' or 'O') if there is a winner, or None otherwise.
    """
    # Define the four directions to check: horizontal, vertical, and two diagonals
    directions = [
        (0, 1),   # horizontal
        (1, 0),   # vertical
        (1, 1),   # diagonal (top-left to bottom-right)
        (1, -1)   # diagonal (top-right to bottom-left)
    ]
    
    # Iterate through each cell on the board
    for row in range(self.size):
        for col in range(self.size):
            # Skip empty cells
            if self.board[row][col] is None:
                continue
            
            current_symbol = self.board[row][col]
            
            # Check in each direction
            for dr, dc in directions:
                count = 1  # Count the current cell
                
                # Check forward in the direction
                r, c = row + dr, col + dc
                while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == current_symbol:
                    count += 1
                    r += dr
                    c += dc
                
                # Check backward in the direction
                r, c = row - dr, col - dc
                while 0 <= r < self.size and 0 <= c < self.size and self.board[r][c] == current_symbol:
                    count += 1
                    r -= dr
                    c -= dc
                
                # If we found 5 or more in a row, we have a winner
                if count >= 5:
                    return current_symbol
    
    return None