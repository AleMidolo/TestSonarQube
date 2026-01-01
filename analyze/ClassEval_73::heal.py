def heal(self):
    """
        Guarisci il personaggio con 10 hp e i hp massimi sono 100.
        :return: int, i punti salute attuali dopo la guarigione.
        >>> player_1 = RPGCharacter('giocatore 1', 93, 10, 3)
        >>> player_1.heal()
        100
        """
    self.hp = min(self.hp + 10, 100)
    return self.hp