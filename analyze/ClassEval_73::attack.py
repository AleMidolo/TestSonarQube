def attack(self, other_character):
    """
        किसी अन्य पात्र पर हमला करें। जो क्षति होती है, उसे रक्षा मूल्य को संतुलित करना चाहिए।
        :param other_character: str, वह पात्र जिसे हमला किया जा रहा है।
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
    if other_character.hp < 0:
        other_character.hp = 0