def check_winner(self, player_hand, dealer_hand):
    """
    Determina el ganador de un juego comparando los valores de las manos del jugador y del dealer.
    regla:
    Si ambos jugadores tienen valores de mano que son iguales o menores a 21, el ganador es aquel cuya mano esté más cerca de 21.
    De lo contrario, el ganador es el que tenga el valor de mano más bajo.
    :param player_hand: lista
    :param dealer_hand: lista
    :return: el resultado del juego, solo dos cadenas ciertas: 'El dealer gana' o 'El jugador gana'
    >>> black_jack_game.check_winner(['QD', '9D', 'JC', 'QH', 'AS'], ['QD', '9D', 'JC', 'QH', '2S'])
    'El jugador gana'
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
    
    # Si ambos tienen 21 o menos, gana el más cercano a 21
    if player_value <= 21 and dealer_value <= 21:
        if player_value > dealer_value:
            return 'El jugador gana'
        else:
            return 'El dealer gana'
    # De lo contrario, gana el que tenga el valor más bajo
    else:
        if player_value < dealer_value:
            return 'El jugador gana'
        else:
            return 'El dealer gana'