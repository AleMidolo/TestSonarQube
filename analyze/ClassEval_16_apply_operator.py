def apply_operator(self, operand_stack, operator_stack):
    """
    Utiliza el operador en la parte superior de la pila de operadores para realizar la operación en los dos números en la parte superior de la pila de operandos, y almacena los resultados en la parte superior de la pila de operandos.
    :param operand_stack:list
    :param operator_stack:list
    :return: la pila de operandos y la pila de operadores actualizadas
    >>> calculator = Calculator()
    >>> calculator.apply_operator([1, 2, 3], ['+', '-'])
    ([1, -1], ['-'])
    """
    if len(operand_stack) < 2 or len(operator_stack) < 1:
        return operand_stack, operator_stack
    
    # Extraer los dos operandos superiores
    operand2 = operand_stack.pop()
    operand1 = operand_stack.pop()
    
    # Extraer el operador superior
    operator = operator_stack.pop()
    
    # Realizar la operación
    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
    elif operator == '//':
        result = operand1 // operand2
    elif operator == '%':
        result = operand1 % operand2
    elif operator == '**':
        result = operand1 ** operand2
    else:
        result = 0
    
    # Almacenar el resultado en la pila de operandos
    operand_stack.append(result)
    
    return operand_stack, operator_stack