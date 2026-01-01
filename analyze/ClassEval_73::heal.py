def heal(self):
    """
        पात्र को 10 एचपी से ठीक करें और अधिकतम एचपी 100 है।
        :return: int, ठीक करने के बाद वर्तमान स्वास्थ्य अंक।
        >>> player_1 = RPGCharacter('player 1', 93, 10, 3)
        >>> player_1.heal()
        100
        """
    self.hp = min(self.hp + 10, 100)
    return self.hp