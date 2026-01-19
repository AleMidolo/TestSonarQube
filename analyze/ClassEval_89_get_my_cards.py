def get_my_cards(self):
    """
    Get a list of four random numbers between 1 and 9 representing the player's cards.
    :return: list of integers, representing the player's cards
    >>> game = TwentyFourPointGame()
    >>> game.get_my_cards()

    """
    import random
    return [random.randint(1, 9) for _ in range(4)]