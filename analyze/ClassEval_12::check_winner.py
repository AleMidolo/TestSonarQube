def check_winner(self, player_hand, dealer_hand):
    """
    Determina il vincitore di un gioco confrontando i valori delle mani del giocatore e del dealer.
    regola:
    Se entrambi i giocatori hanno valori delle mani che sono uguali o inferiori a 21, il vincitore è colui il cui valore della mano è più vicino a 21.
    Altrimenti, il vincitore è colui che ha il valore della mano più basso.
    :param player_hand: lista
    :param dealer_hand: lista
    :return: il risultato del gioco, solo due stringhe certe: 'Il dealer vince' o 'Il giocatore vince'
    >>> black_jack_game.check_winner(['QD', '9D', 'JC', 'QH', 'AS'], ['QD', '9D', 'JC', 'QH', '2S'])
    'Il giocatore vince'
    """
    player_value = self.calculate_hand_value(player_hand)
    dealer_value = self.calculate_hand_value(dealer_hand)
    if player_value > 21 and dealer_value > 21:
        return 'Il dealer vince'
    elif player_value > 21:
        return 'Il dealer vince'
    elif dealer_value > 21:
        return 'Il giocatore vince'
    elif player_value > dealer_value:
        return 'Il giocatore vince'
    elif dealer_value > player_value:
        return 'Il dealer vince'
    else:
        return 'Il dealer vince'