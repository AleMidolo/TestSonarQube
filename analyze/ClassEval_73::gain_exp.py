def gain_exp(self, amount):
    """
        Guadagna punti esperienza per il personaggio e aumenta di livello quando l'esperienza ha raggiunto i valori che sono 100 volte il livello attuale.
        L'esperienza in eccesso dovrebbe essere utilizzata per calcolare il prossimo aumento di livello fino a esaurirsi.
        :param amount: int, la quantità di punti esperienza da guadagnare.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.gain_exp(1100)
        >>> player_1.exp
        100
        >>> player_1.level
        5
        """
    self.exp += amount
    while self.exp >= 100 * self.level:
        self.exp -= 100 * self.level
        self.level_up()