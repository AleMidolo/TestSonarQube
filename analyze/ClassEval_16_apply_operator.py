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
    operator = operator_stack.pop()
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    result = self.operators[operator](left_operand, right_operand)
    operand_stack.append(result)
    return (operand_stack, operator_stack)