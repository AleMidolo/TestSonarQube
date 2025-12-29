def evaluate_expression(self, expression):
    """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression equals 24, otherwise False
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    try:
        result = eval(expression, {'__builtins__': None}, {})
        return abs(result - 24) < 1e-10
    except:
        return False