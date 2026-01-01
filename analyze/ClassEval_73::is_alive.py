def is_alive(self):
    """
        检查玩家是否存活。
        :return: 如果生命值大于0则返回True，否则返回False。
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.is_alive()
        True
        """
    return self.hp > 0