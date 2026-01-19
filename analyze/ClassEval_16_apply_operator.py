def apply_operator(self, operand_stack, operator_stack):
    """
    Utilizza l'operatore in cima allo stack degli operatori per eseguire l'operazione sui due numeri in cima allo stack degli operandi, e memorizza i risultati in cima allo stack degli operatori
    :param operand_stack:list
    :param operator_stack:list
    :return: lo stack degli operandi e lo stack degli operatori aggiornati
    >>> calculator = Calculator()
    >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
    ([1, -1], ['-'])
    """
    if len(operand_stack) < 2 or len(operator_stack) < 1:
        return operand_stack, operator_stack
    
    # Pop the top operator
    operator = operator_stack.pop()
    
    # Pop the top two operands (second operand is popped first)
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    
    # Apply the operation
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    else:
        result = 0
    
    # Push the result back to operand stack
    operand_stack.append(result)
    
    return operand_stack, operator_stack