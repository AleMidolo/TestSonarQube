def calculate_hand_value(self, hand):
    """
    Calcola il valore delle carte da poker memorizzate nella lista hand secondo le regole del Gioco del Blackjack.
    Se la carta è un numero, il suo valore viene aggiunto al valore totale della mano.
    Il valore di J, Q o K è 10, mentre gli Assi valgono 11.
    Se il valore totale della mano supera 21 e ci sono Assi presenti, un Asso viene considerato avere un valore di 1 invece di 11,
    fino a quando il valore della mano è minore o uguale a 21, o tutti gli Assi sono stati conteggiati come valore di 1.
    :param hand: lista
    :return: il valore delle carte da poker memorizzate nella lista hand, un numero.
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
            value += 11
            aces += 1
        else:
            value += int(rank)
    
    # Adjust for Aces if value exceeds 21
    while value > 21 and aces:
        value -= 10
        aces -= 1
    
    return value