def is_alive(self):
    """
        Controlla se il giocatore è vivo.
        :return: True se i punti vita (hp) sono maggiori di 0, altrimenti False.
        >>> player_1 = RPGCharacter('giocatore 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """
    return self.hp > 0