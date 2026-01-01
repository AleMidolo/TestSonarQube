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
    import re
    numbers_in_expr = re.findall('\\d+\\.?\\d*', expression)
    numbers_in_expr = [int(num) if '.' not in num else float(num) for num in numbers_in_expr]
    if sorted(numbers_in_expr) != sorted(self.nums):
        return False
    return self.evaluate_expression(expression)