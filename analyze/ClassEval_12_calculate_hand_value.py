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
    total_value = 0
    aces_count = 0
    
    for card in hand:
        # Estrai il valore della carta (tutti i caratteri tranne l'ultimo che è il seme)
        rank = card[:-1]
        
        if rank in ['J', 'Q', 'K']:
            total_value += 10
        elif rank == 'A':
            total_value += 11
            aces_count += 1
        else:
            total_value += int(rank)
    
    # Aggiusta il valore degli Assi se necessario
    while total_value > 21 and aces_count > 0:
        total_value -= 10  # Cambia un Asso da 11 a 1 (sottrai 10)
        aces_count -= 1
    
    return total_value