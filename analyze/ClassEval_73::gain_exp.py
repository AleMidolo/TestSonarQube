def gain_exp(self, amount):
    """
        为角色获得经验值，当经验值达到当前等级的100倍时升级。
        溢出的经验值应用于计算下一个升级，直到耗尽。
        :param amount: int，获得的经验值数量。
        >>> player_1 = RPGCharacter('player 1', 100, 10, 3)
        >>> player_1.gain_exp(1100)
        >>> player_1.exp
        100
        >>> player_1.level
        5
        """
    remaining_exp = amount
    while remaining_exp > 0 and self.level < 100:
        exp_needed = self.level * 100
        exp_to_next_level = exp_needed - self.exp
        if remaining_exp >= exp_to_next_level:
            remaining_exp -= exp_to_next_level
            self.level_up()
        else:
            self.exp += remaining_exp
            remaining_exp = 0