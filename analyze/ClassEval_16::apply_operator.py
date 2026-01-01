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
    operator = operator_stack.pop()
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    result = self.operators[operator](left_operand, right_operand)
    operand_stack.append(result)
    return (operand_stack, operator_stack)