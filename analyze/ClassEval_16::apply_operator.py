def apply_operator(self, operand_stack, operator_stack):
    """
        Utilizes the operator on top of the operator stack to perform the operation on the two numbers on top of the operand stack, and stores the results on top of the operand stack
        :param operand_stack: list
        :param operator_stack: list
        :return: the updated operand stack and operator stack
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