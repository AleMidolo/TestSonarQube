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
    numbers_in_expr = re.findall('-?\\d+\\.?\\d*', expression)
    numbers_in_expr = [float(num) for num in numbers_in_expr]
    numbers_in_expr = [int(num) if num.is_integer() else num for num in numbers_in_expr]
    expr_counter = Counter(numbers_in_expr)
    nums_counter = Counter(self.nums)
    for num, count in expr_counter.items():
        if nums_counter[num] < count:
            return False
    total_used = sum(expr_counter.values())
    if total_used != 4:
        return False
    if expr_counter != nums_counter:
        return False
    return True