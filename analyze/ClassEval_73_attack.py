def attack(self, other_character):
    """
        攻击另一个角色。造成的伤害需要扣除防御值。
        :param other_character: str, 被攻击的角色。
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_2 = RPGCharacter('player 2', 100, 7, 2)
        >>> player_1.attack(player_2)
        >>> player_2.hp
        92
        """
    damage = self.attack_power - other_character.defense
    if damage < 0:
        damage = 0
    other_character.hp -= damage