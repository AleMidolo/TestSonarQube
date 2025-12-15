def get_my_cards(self):
        """
        获取一个包含四个介于1到9之间的随机数字的列表，代表玩家的牌。
        :return: 整数列表，代表玩家的牌
        >>> game = TwentyFourPointGame()
        >>> game.get_my_cards()
        """
        self.nums = []
        self._generate_cards()
        return self.nums