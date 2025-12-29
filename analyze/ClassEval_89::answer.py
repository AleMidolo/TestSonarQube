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
    try:
        import re
        expr_numbers = re.findall('\\d+', expression)
        expr_numbers = [int(num) for num in expr_numbers]
        if sorted(expr_numbers) == sorted(self.nums):
            return True
        else:
            return False
    except Exception as e:
        return False