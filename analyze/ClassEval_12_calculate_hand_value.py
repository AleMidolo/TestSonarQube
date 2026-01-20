def calculate_hand_value(self, hand):
    """
    Calcular el valor de las cartas de póker almacenadas en la lista de mano de acuerdo con las reglas del juego de Blackjack.
    Si la carta es un dígito, su valor se suma al valor total de la mano.
    El valor de J, Q o K es 10, mientras que los Ases valen 11.
    Si el valor total de la mano excede 21 y hay Ases presentes, un As se considera con un valor de 1 en lugar de 11,
    hasta que el valor de la mano sea menor o igual a 21, o todos los Ases se hayan contado como valor de 1.
    :param hand: lista
    :return: el valor de las cartas de póker almacenadas en la lista de mano, un número.
    >>> black_jack_game.calculate_hand_value(['QD', '9D', 'JC', 'QH', 'AS'])
    40
    """
    total_value = 0
    aces_count = 0
    
    for card in hand:
        # Extraer el rango de la carta (primer(os) carácter(es) antes del palo)
        rank = card[:-1]  # Todos los caracteres excepto el último (que es el palo)
        
        if rank in ['J', 'Q', 'K']:
            total_value += 10
        elif rank == 'A':
            total_value += 11
            aces_count += 1
        else:
            # Es un dígito (2-10)
            total_value += int(rank)
    
    # Ajustar el valor de los Ases si es necesario
    while total_value > 21 and aces_count > 0:
        total_value -= 10  # Cambiar un As de 11 a 1 (restar 10)
        aces_count -= 1
    
    return total_value