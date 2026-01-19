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
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    
    operand_stack.append(result)
    
    return (operand_stack, operator_stack)