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
    # Calculate hand values
    player_value = self.calculate_hand_value(player_hand)
    dealer_value = self.calculate_hand_value(dealer_hand)
    
    # Check if both hands are 21 or less
    if player_value <= 21 and dealer_value <= 21:
        # Winner is the one closer to 21 (higher value)
        if player_value > dealer_value:
            return 'Player wins'
        else:
            return 'Dealer wins'
    # If both are over 21, winner has lower value
    elif player_value > 21 and dealer_value > 21:
        if player_value < dealer_value:
            return 'Player wins'
        else:
            return 'Dealer wins'
    # If only player is over 21, dealer wins
    elif player_value > 21:
        return 'Dealer wins'
    # If only dealer is over 21, player wins
    else:
        return 'Player wins'