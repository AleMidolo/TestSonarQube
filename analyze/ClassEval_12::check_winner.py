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
    player_value = self.calculate_hand_value(player_hand)
    dealer_value = self.calculate_hand_value(dealer_hand)
    if player_value > 21 and dealer_value > 21:
        return 'El dealer gana' if dealer_value <= player_value else 'El jugador gana'
    if player_value > 21:
        return 'El dealer gana'
    if dealer_value > 21:
        return 'El jugador gana'
    if player_value > dealer_value:
        return 'El jugador gana'
    else:
        return 'El dealer gana'