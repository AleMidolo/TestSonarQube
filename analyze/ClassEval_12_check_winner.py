def check_winner(self, player_hand, dealer_hand):
    """
    通过比较玩家和庄家的手牌点数来确定游戏的赢家。
    规则：
    如果两个玩家的手牌点数都小于或等于21，则赢家是手牌点数更接近21的那一方。
    否则，赢家是手牌点数较低的那一方。
    :param player_hand: list
    :param dealer_hand: list
    :return: 游戏结果，只能是两种字符串：'Dealer wins' 或 'Player wins'
    >>> black_jack_game.check_winner(['QD', '9D', 'JC', 'QH', 'AS'], ['QD', '9D', 'JC', 'QH', '2S'])
    'Player wins'
    """
    player_score = self.calculate_hand_value(player_hand)
    dealer_score = self.calculate_hand_value(dealer_hand)
    
    # 如果两个玩家的手牌点数都小于或等于21
    if player_score <= 21 and dealer_score <= 21:
        # 赢家是手牌点数更接近21的那一方
        if player_score > dealer_score:
            return 'Player wins'
        else:
            return 'Dealer wins'
    else:
        # 否则，赢家是手牌点数较低的那一方
        if player_score < dealer_score:
            return 'Player wins'
        else:
            return 'Dealer wins'