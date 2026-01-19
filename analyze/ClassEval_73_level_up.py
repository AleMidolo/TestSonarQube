def level_up(self):
    """
        Aumenta el nivel del personaje y devuelve a cero los puntos de experiencia, aumenta los puntos de salud en 20, el poder de ataque y los puntos de defensa en 5.
        El nivel máximo es 100.
        :return: tuple[int, int, int, int], el nuevo nivel, puntos de salud, poder de ataque y puntos de defensa después de subir de nivel.
        >>> player_1 = RPGCharacter('jugador 1', 100, 10, 3)
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