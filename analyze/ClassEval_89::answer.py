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
    import re
    nums_in_expr = re.findall('\\d+', expression)
    nums_in_expr = [int(num) for num in nums_in_expr]
    if sorted(nums_in_expr) != sorted(self.nums):
        return False
    return self.evaluate_expression(expression)