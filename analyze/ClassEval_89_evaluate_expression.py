def evaluate_expression(self, expression):
    """
        Evalúa una expresión matemática y verifica si el resultado es 24.
        :param expression: cadena, expresión matemática
        :return: bool, True si la expresión evalúa a 24, False en caso contrario
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    try:
        result = eval(expression)
        return math.isclose(result, 24, rel_tol=1e-09)
    except:
        return False