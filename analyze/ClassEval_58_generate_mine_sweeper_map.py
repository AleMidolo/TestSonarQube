def generate_mine_sweeper_map(self):
    """
    दिए गए बोर्ड के आकार और खानों की संख्या के साथ एक माइनस्वीपर मानचित्र उत्पन्न करता है, 
    दिए गए पैरामीटर n बोर्ड का आकार है, बोर्ड का आकार n*n है, 
    पैरामीटर k खानों की संख्या है, 'X' खान का प्रतिनिधित्व करता है, 
    अन्य संख्याएँ स्थिति के चारों ओर खानों की संख्या का प्रतिनिधित्व करती हैं।
    :return: माइनस्वीपर मानचित्र, सूची।
    >>> minesweeper_game = MinesweeperGame(3, 1)
    >>> minesweeper_game.generate_mine_sweeper_map()
    [['X', 1, 0], [1, 1, 0], [0, 0, 0]]

    """
    import random
    
    # Initialize the board with zeros
    board = [[0 for _ in range(self.n)] for _ in range(self.n)]
    
    # Place mines randomly
    mines_placed = 0
    while mines_placed < self.k:
        row = random.randint(0, self.n - 1)
        col = random.randint(0, self.n - 1)
        
        # Only place mine if cell doesn't already have one
        if board[row][col] != 'X':
            board[row][col] = 'X'
            mines_placed += 1
    
    # Calculate numbers for non-mine cells
    for i in range(self.n):
        for j in range(self.n):
            if board[i][j] != 'X':
                # Count adjacent mines
                mine_count = 0
                # Check all 8 adjacent cells
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < self.n and 0 <= nj < self.n:
                            if board[ni][nj] == 'X':
                                mine_count += 1
                board[i][j] = mine_count
    
    return board