def level_up(self):
    """
        Increase the character's level, reset experience points to zero, increase health points by 20, attack power and defense points by 5.
        The maximum level is 100.
        :return: tuple[int, int, int, int], the new level, health points, attack power, and defense points after leveling up.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """
    if self.level < 100:
        self.level += 1
        self.exp = 0
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
        if self.hp > 100:
            self.hp = 100
    return (self.level, self.hp, self.attack_power, self.defense)