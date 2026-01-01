def answer(self, expression):
    """
        检查给定的数学表达式是否可以使用这些牌计算出24。
        :param expression: 字符串，使用牌的数学表达式
        :return: 布尔值，如果表达式计算结果为24则返回True，否则返回False
        >>> game = TwentyFourPointGame()
        >>> game.nums = [4, 3, 6, 6]
        >>> ans = "4*3+6+6"
        >>> ret = game.answer(ans)
        True
        """
    if not self.evaluate_expression(expression):
        return False
    import re
    numbers_in_expr = re.findall('\\d+', expression)
    numbers_in_expr = [int(num) for num in numbers_in_expr]
    if Counter(numbers_in_expr) != Counter(self.nums):
        return False
    return True