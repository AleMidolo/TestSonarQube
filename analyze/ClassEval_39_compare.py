def compare(self, cur, peek):
    """
        比较两个运算符的优先级
        :param cur: 字符串，当前运算符
        :param peek: 字符串，运算符栈顶部的运算符
        :return: 布尔值，如果当前运算符具有更高或相等的优先级，则为 True，否则为 False
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True

        """
    op_map = {'+': 0, '-': 1, '*': 2, '/': 3, '(': 4, ')': 5, '#': 6, '%': 7}
    if cur not in op_map or peek not in op_map:
        return False
    cur_priority = self.operat_priority[op_map[cur]]
    peek_priority = self.operat_priority[op_map[peek]]
    return cur_priority <= peek_priority