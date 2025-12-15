def calculate_hand_value(self, hand):
        """
        根据 Blackjack（21 点）游戏的规则计算手牌的点数。
        如果牌面是数字牌，则其对应数值直接加入总点数。
        J、Q、K 的点数为 10，而 A 算作 11。
        如果总点数超过 21 且手中含有 A，则将其中一张 A 的点数由 11 改为 1，
        直到总点数不超过 21，或所有 A 都已按 1 计算为止。
        :param hand: list
        :return: 一个数字，手牌的总点数。
        >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
        40
        """
        value = 0
        aces = 0
        
        for card in hand:
            rank = card[:-1]  # Get the rank of the card
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                aces += 1
                value += 11  # Initially count Ace as 11
            else:
                value += int(rank)  # Add the numeric value of the card
        
        # Adjust for Aces if value exceeds 21
        while value > 21 and aces > 0:
            value -= 10  # Change one Ace from 11 to 1
            aces -= 1
        
        return value