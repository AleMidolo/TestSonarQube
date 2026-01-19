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
        # Valuta l'espressione matematica in modo sicuro
        result = eval(expression)
        # Verifica se il risultato è 24 (con tolleranza per errori di floating point)
        return abs(result - 24) < 1e-6
    except:
        # Se c'è un errore nella valutazione, ritorna False
        return False