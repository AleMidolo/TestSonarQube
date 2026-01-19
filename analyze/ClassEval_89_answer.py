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
    try:
        # Extract all numbers from the expression
        import re
        numbers_in_expr = re.findall(r'\d+', expression)
        numbers_in_expr = [int(n) for n in numbers_in_expr]
        
        # Check if the numbers used match the available cards
        nums_sorted = sorted(self.nums)
        expr_sorted = sorted(numbers_in_expr)
        
        if nums_sorted != expr_sorted:
            return False
        
        # Evaluate the expression
        result = eval(expression)
        
        # Check if result equals 24 (with floating point tolerance)
        return abs(result - 24) < 1e-6
        
    except:
        return False