def level_up(self):
    """
    升级角色并将经验值重置为零，生命值增加20点，攻击力和防御力各增加5点。
    最大等级为100
    :return: tuple[int, int, int, int]，升级后的新等级、生命值、攻击力和防御力。
    >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
    >>> player_1.level_up()
    (2, 120, 15, 8)
    """
    if self.level < 100:
        self.level += 1
    self.experience = 0
    self.health += 20
    self.attack += 5
    self.defense += 5
    return (self.level, self.health, self.attack, self.defense)