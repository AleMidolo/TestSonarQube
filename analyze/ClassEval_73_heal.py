def heal(self):
    """
    为角色恢复10点生命值,最大生命值为100。
    :return: int,治疗后当前的生命值。
    >>> player_1 = RPGCharacter('player 1', 93, 10, 3)
    >>> player_1.heal()
    100
    """
    self.health = min(self.health + 10, 100)
    return self.health