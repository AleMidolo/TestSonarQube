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
    except Exception:
        operand_stack.append(a)
        operand_stack.append(b)
        operator_stack.append(operator)
    return (operand_stack, operator_stack)