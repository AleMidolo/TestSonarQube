def is_alive(self):
    """
    Verifica si el jugador está vivo.
    :return: True si los hp son mayores que 0, o False en caso contrario.
    >>> player_1 = RPGCharacter('jugador 1', 100, 10, 3)
    >>> player_1.is_alive()
    True
    """
    return self.hp > 0