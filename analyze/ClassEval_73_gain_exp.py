def gain_exp(self, amount):
    """
    Gana puntos de experiencia para el personaje y sube de nivel cuando la experiencia ha alcanzado los valores que son 100 veces el nivel actual.
    La experiencia que desborda debe ser utilizada para calcular el siguiente nivel hasta que se agote.
    :param amount: int, la cantidad de puntos de experiencia a ganar.
    >>> player_1 = RPGCharacter('jugador 1', 100, 10, 3)
    >>> player_1.gain_exp(1100)
    >>> player_1.exp
    100
    >>> player_1.level
    5
    """
    self.exp += amount
    
    while self.exp >= 100 * self.level:
        self.exp -= 100 * self.level
        self.level += 1