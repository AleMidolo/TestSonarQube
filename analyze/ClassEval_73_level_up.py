def level_up(self):
    """
        Aumenta di livello il personaggio e riporta a zero i punti esperienza, aumenta i punti vita di 20, la potenza d'attacco e i punti difesa di 5.
        Il livello massimo è 100.
        :return: tuple[int, int, int, int], il nuovo livello, i punti vita, la potenza d'attacco e i punti difesa dopo l'aumento di livello.
        >>> player_1 = RPGCharacter('giocatore 1', 100, 10, 3)
        >>> player_1.level_up()
        (2, 120, 15, 8)
        """
    if self.level < 100:
        self.level += 1
        self.exp = 0
        self.hp += 20
        self.attack_power += 5
        self.defense += 5
    return (self.level, self.hp, self.attack_power, self.defense)