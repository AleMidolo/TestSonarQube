def evaluate_expression(self, expression):
    """
    Valuta un'espressione matematica e verifica se il risultato è 24.
    :param expression: stringa, espressione matematica
    :return: bool, True se l'espressione si valuta a 24, False altrimenti
    >>> game = TwentyFourPointGame()
    >>> nums = [4, 3, 6, 6]
    >>> ans = "4*3+6+6"
    >>> ret = game.evaluate_expression(ans)
    True
    """
    try:
        result = eval(expression)
        return abs(result - 24) < 1e-6
    except:
        return False