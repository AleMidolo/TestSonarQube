def answer(self, expression):
    """
        Controlla se una data espressione matematica usando le carte può valutarsi a 24.
        :param expression: stringa, espressione matematica usando le carte
        :return: bool, True se l'espressione si valuta a 24, False altrimenti
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.answer(ans)
        True
        """
    if not self.evaluate_expression(expression):
        return False
    import re
    numbers_in_expr = re.findall('\\d', expression)
    numbers_in_expr = [int(num) for num in numbers_in_expr]
    if len(numbers_in_expr) != 4:
        return False
    return sorted(numbers_in_expr) == sorted(self.nums)