def attack(self, other_character):
    """
        Atacar a otro personaje. El daño causado debe compensar el valor de defensa.
        :param other_character: str, El personaje que está siendo atacado.
        >>> player_1 = RPGCharacter('jugador 1', 100, 10, 3)
        >>> player_2 = RPGCharacter('jugador 2', 100, 7, 2)
        >>> player_1.attack(player_2)
        >>> player_2.hp
        92
        """
    damage = self.attack_power - other_character.defense
    if damage < 0:
        damage = 0
    other_character.hp -= damage