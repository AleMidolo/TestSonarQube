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
    board = [[0 for _ in range(self.n)] for _ in range(self.n)]
    mines_placed = 0
    while mines_placed < self.k:
        x = random.randint(0, self.n - 1)
        y = random.randint(0, self.n - 1)
        if board[x][y] != 'X':
            board[x][y] = 'X'
            mines_placed += 1
    for i in range(self.n):
        for j in range(self.n):
            if board[i][j] == 'X':
                continue
            mine_count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ni, nj = (i + dx, j + dy)
                    if 0 <= ni < self.n and 0 <= nj < self.n:
                        if board[ni][nj] == 'X':
                            mine_count += 1
            board[i][j] = mine_count
    return board