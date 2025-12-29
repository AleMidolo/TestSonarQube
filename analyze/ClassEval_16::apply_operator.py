def apply_operator(self, operand_stack, operator_stack):
    """
        Use the operator at the top of the operator stack to perform the operation on the two numbers at the top of the operator stack, and store the results at the top of the operator stack
        :param operand_stack:list
        :param operator_stack:list
        :return: the updated operand_stack and operator_stack
        >>> calculator = Calculator()
        >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
        ([1, -1], ['-'])
        """
    if len(operand_stack) < 2 or not operator_stack:
        return (operand_stack, operator_stack)
    operator = operator_stack.pop()
    b = operand_stack.pop()
    a = operand_stack.pop()
    try:
        result = self.operators[operator](a, b)
        operand_stack.append(result)
    except ZeroDivisionError:
        operand_stack.append(float('inf') if a > 0 else float('-inf'))
    return (operand_stack, operator_stack)