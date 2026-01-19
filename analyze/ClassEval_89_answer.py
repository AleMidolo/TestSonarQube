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
        numbers_in_expr = []
        for num in re.findall(r'\d+', expression):
            numbers_in_expr.append(int(num))
        
        # Sort both lists to compare
        numbers_in_expr.sort()
        nums_sorted = sorted(self.nums)
        
        # Check if the numbers used match the available cards
        if numbers_in_expr != nums_sorted:
            return False
        
        # Evaluate the expression
        result = eval(expression)
        
        # Check if result equals 24 (with floating point tolerance)
        return abs(result - 24) < 1e-9
    except:
        return False