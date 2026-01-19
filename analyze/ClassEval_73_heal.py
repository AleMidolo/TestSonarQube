def heal(self):
    """
    Cura al personaje con 10 hp y el hp máximo es 100.
    :return: int, los puntos de salud actuales después de curar.
    >>> player_1 = RPGCharacter('jugador 1', 93, 10, 3)
    >>> player_1.heal()
    100
    """
    self.hp = min(self.hp + 10, 100)
    return self.hp