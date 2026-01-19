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
    def calculate_hand_value(hand):
        value = 0
        aces = 0
        
        for card in hand:
            rank = card[:-1]  # Rimuove il seme (ultimo carattere)
            
            if rank in ['J', 'Q', 'K']:
                value += 10
            elif rank == 'A':
                aces += 1
                value += 11
            else:
                value += int(rank)
        
        # Aggiusta il valore degli assi se necessario
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        
        return value
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    # Se entrambi <= 21, vince chi è più vicino a 21
    if player_value <= 21 and dealer_value <= 21:
        if player_value >= dealer_value:
            return 'Il giocatore vince'
        else:
            return 'Il dealer vince'
    # Altrimenti, vince chi ha il valore più basso
    else:
        if player_value <= dealer_value:
            return 'Il giocatore vince'
        else:
            return 'Il dealer vince'