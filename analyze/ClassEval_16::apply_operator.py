def apply_operator(self, operand_stack, operator_stack):
    """
        使用操作符栈顶部的操作符对操作数栈顶部的两个数字执行操作，并将结果存储在操作数栈顶部
        :param operand_stack:list
        :param operator_stack:list
        :return: 更新后的 operand_stack 和 operator_stack
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['-'])
        """
    if len(operand_stack) < 2 or not operator_stack:
        return (operand_stack, operator_stack)
    operator = operator_stack.pop()
    b = operand_stack.pop()
    a = operand_stack.pop()
    if operator in self.operators:
        try:
            result = self.operators[operator](a, b)
            operand_stack.append(result)
        except ZeroDivisionError:
            operand_stack.append(float('inf') if a > 0 else float('-inf'))
    return (operand_stack, operator_stack)