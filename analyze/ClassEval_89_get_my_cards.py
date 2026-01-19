def get_my_cards(self):
    """
    Obtiene una lista de cuatro números aleatorios entre 1 y 9 que representan las cartas del jugador.
    :return: lista de enteros, que representan las cartas del jugador
    >>> juego = TwentyFourPointGame()
    >>> juego.get_my_cards()

    """
    import random
    return [random.randint(1, 9) for _ in range(4)]