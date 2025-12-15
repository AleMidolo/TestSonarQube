def answer(self, expression):
    """
    Check if a given mathematical expression using the cards can evaluate to 24.
    :param expression: string, mathematical expression using the cards
    :return: bool, True if the expression evaluates to 24, False otherwise
    >>> game = TwentyFourPointGame()
    >>> game.nums = [4, 3, 6, 6]
    >>> ans = "4*3+6+6"
    >>> ret = game.answer(ans)
    True
    """
    
    return self.evaluate_expression(expression)