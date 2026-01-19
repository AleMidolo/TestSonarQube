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
    positions = [(i, j) for i in range(self.n) for j in range(self.n)]
    random.shuffle(positions)
    
    for i in range(self.k):
        row, col = positions[i]
        board[row][col] = 'X'
    
    # Calculate numbers for non-mine cells
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    for i in range(self.n):
        for j in range(self.n):
            if board[i][j] != 'X':
                mine_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < self.n and 0 <= nj < self.n and board[ni][nj] == 'X':
                        mine_count += 1
                board[i][j] = mine_count
    
    return board