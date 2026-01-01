def create_deck(self):
    """
    Crea una baraja de 52 cartas, que almacena 52 cartas de póker en orden aleatorio con los Jokers eliminados.
    :return: una lista de 52 cartas de póker en orden aleatorio con los Jokers eliminados, el formato es ['AS', '2S', ...].
    >>> black_jack_game = BlackjackGame()
    >>> black_jack_game.create_deck()
    ['QD', '9D', 'JC', 'QH', '2S', 'JH', '7D', '6H', '9S', '5C', '7H', 'QS', '5H',
    '6C', '7C', '3D', '10C', 'AD', '4C', '5D', 'AH', '2D', 'QC', 'KH', '9C', '9H',
    '4H', 'JS', '6S', '8H', '8C', '4S', '3H', '10H', '7S', '6D', '3C', 'KC', '3S',
    '2H', '10D', 'KS', '4D', 'AC', '10S', '2C', 'KD', '5S', 'JD', '8S', 'AS', '8D']
    """
    suits = ['H', 'D', 'C', 'S']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [rank + suit for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck