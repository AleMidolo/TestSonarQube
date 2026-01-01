def check_winner(self, player_hand, dealer_hand):
    """
        खेल के विजेता का निर्धारण करता है खिलाड़ी और डीलर के हाथ के मानों की तुलना करके।
        नियम:
        यदि दोनों खिलाड़ियों के हाथ के मान 21 के बराबर या उससे कम हैं, तो विजेता वह है जिसका हाथ का मान 21 के करीब है।
        अन्यथा, विजेता वह है जिसके पास कम हाथ का मान है।
        :param player_hand: सूची
        :param dealer_hand: सूची
        :return: खेल का परिणाम, केवल दो निश्चित स्ट्रिंग: 'Dealer wins' या 'Player wins'
        >>> black_jack_game.check_winner(['QD', '9D', 'JC', 'QH', 'AS'], ['QD', '9D', 'JC', 'QH', '2S'])
        'Player wins'
        """
    player_value = self.calculate_hand_value(player_hand)
    dealer_value = self.calculate_hand_value(dealer_hand)
    if player_value <= 21 and dealer_value <= 21:
        if player_value > dealer_value:
            return 'Player wins'
        elif dealer_value > player_value:
            return 'Dealer wins'
        else:
            return 'Dealer wins'
    elif player_value > 21 and dealer_value > 21:
        if player_value < dealer_value:
            return 'Player wins'
        else:
            return 'Dealer wins'
    elif player_value > 21:
        return 'Dealer wins'
    else:
        return 'Player wins'