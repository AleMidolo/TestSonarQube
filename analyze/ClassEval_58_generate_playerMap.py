def generate_playerMap(self):
    """
        दिए गए बोर्ड के आकार के साथ एक खिलाड़ी मानचित्र उत्पन्न करता है, दिए गए पैरामीटर n बोर्ड का आकार है, बोर्ड का आकार n*n है, पैरामीटर k खानों की संख्या है, '-' अज्ञात स्थिति का प्रतिनिधित्व करता है।
        :return: खिलाड़ी मानचित्र, सूची।
        >>> minesweeper_game = MinesweeperGame(3, 1)
        >>> minesweeper_game.generate_playerMap()
        [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

        """
    return [['-' for _ in range(self.n)] for _ in range(self.n)]