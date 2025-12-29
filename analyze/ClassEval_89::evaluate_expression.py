def evaluate_expression(self, expression):
    """
        Evaluate a mathematical expression and check if the result is 24.
        :param expression: string, mathematical expression
        :return: bool, True if the expression evaluates to 24, False otherwise
        >>> game = TwentyFourPointGame()
        >>> nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.evaluate_expression(ans)
        True
        """
    try:
        expr = expression.replace('^', '**')
        result = eval(expr, {'__builtins__': {}}, {})
        return abs(result - 24) < 1e-10
    except (SyntaxError, ZeroDivisionError, TypeError, NameError):
        return False