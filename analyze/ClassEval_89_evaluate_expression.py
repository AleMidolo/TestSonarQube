def evaluate_expression(self, expression):
    """
        Evalúa una expresión matemática y verifica si el resultado es 24.
        :param expression: cadena, expresión matemática
        :return: bool, True si la expresión evalúa a 24, False en caso contrario
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    try:
        result = eval(expression, {'__builtins__': {}}, {'math': math})
        return abs(result - 24) < 1e-10
    except (ZeroDivisionError, SyntaxError, NameError, TypeError):
        return False