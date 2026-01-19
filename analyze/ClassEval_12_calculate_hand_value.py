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
    total = 0
    aces = 0
    
    for card in hand:
        # 获取牌面值（去掉花色，取第一个或前两个字符）
        rank = card[:-1]  # 去掉最后一个字符（花色）
        
        if rank in ['J', 'Q', 'K']:
            total += 10
        elif rank == 'A':
            total += 11
            aces += 1
        else:
            total += int(rank)
    
    # 如果总点数超过 21 且有 A，将 A 从 11 改为 1
    while total > 21 and aces > 0:
        total -= 10  # 将一个 A 从 11 改为 1（减去 10）
        aces -= 1
    
    return total