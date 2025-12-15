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
        # Initialize the minesweeper map with zeros
        minesweeper_map = [[0 for _ in range(self.n)] for _ in range(self.n)]
        
        # Place mines randomly
        mines_placed = 0
        while mines_placed < self.k:
            x = random.randint(0, self.n - 1)
            y = random.randint(0, self.n - 1)
            if minesweeper_map[x][y] != 'X':  # Ensure we don't place a mine on an existing mine
                minesweeper_map[x][y] = 'X'
                mines_placed += 1
                
                # Update the surrounding numbers
                for i in range(max(0, x - 1), min(self.n, x + 2)):
                    for j in range(max(0, y - 1), min(self.n, y + 2)):
                        if minesweeper_map[i][j] != 'X':
                            minesweeper_map[i][j] += 1
        
        return minesweeper_map