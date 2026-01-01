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
    operator = operator_stack.pop()
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    result = self.operators[operator](left_operand, right_operand)
    operand_stack.append(result)
    return (operand_stack, operator_stack)