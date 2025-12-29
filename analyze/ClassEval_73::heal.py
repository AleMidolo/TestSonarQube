def heal(self):
    """
        Heal the character by 10 HP with a maximum HP of 100.
        :return: int, the current health points after healing.
        >>> player_1 = RPGCharacter('player 1', 93, 10, 3)
        >>> player_1.heal()
        100
        """
    self.hp = min(self.hp + 10, 100)
    return self.hp