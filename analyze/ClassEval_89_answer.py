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
        numbers_in_expr = [int(num) for num in numbers_in_expr]
        
        # Check if the numbers used match the available cards
        # Sort both lists to compare
        if sorted(numbers_in_expr) != sorted(self.nums):
            return False
        
        # Evaluate the expression
        result = eval(expression)
        
        # Check if result equals 24 (with some tolerance for floating point)
        return abs(result - 24) < 1e-9
    except:
        return False