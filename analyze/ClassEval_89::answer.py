def answer(self, expression):
    """
        Verifica si una expresión matemática dada utilizando las cartas puede evaluarse a 24.
        :param expression: cadena, expresión matemática utilizando las cartas
        :return: bool, True si la expresión se evalúa a 24, False en caso contrario
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.answer(ans)
        True
        """
    return self.evaluate_expression(expression)