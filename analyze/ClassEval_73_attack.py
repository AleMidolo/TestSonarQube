def attack(self, other_character):
    """
        Attack another character. The damage caused needs to offset the defense value.
        :param other_character: str, The character being attacked.
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_2 = RPGCharacter('player 2', 100, 7, 2)
        >>> player_1.attack(player_2)
        >>> player_2.hp
        92
        """
    damage = self.attack_power - other_character.defense
    if damage > 0:
        other_character.hp -= damage
    return other_character.hp