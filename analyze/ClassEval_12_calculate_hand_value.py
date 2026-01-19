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
    value = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            value += 11
            aces += 1
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value