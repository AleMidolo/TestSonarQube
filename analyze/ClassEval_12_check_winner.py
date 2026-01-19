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
    def calculate_hand_value(hand):
        value = 0
        aces = 0
        
        for card in hand:
            rank = card[:-1]  # Remove suit (last character)
            
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                aces += 1
                value += 11
            else:
                value += int(rank)
        
        # Adjust for aces if value exceeds 21
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        
        return value
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    # If both hands are 21 or less, winner is closer to 21
    if player_value <= 21 and dealer_value <= 21:
        if player_value > dealer_value:
            return 'Player wins'
        else:
            return 'Dealer wins'
    # Otherwise, winner has the lower hand value
    else:
        if player_value < dealer_value:
            return 'Player wins'
        else:
            return 'Dealer wins'