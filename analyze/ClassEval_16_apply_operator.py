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
            operand_stack.append(float('inf'))
    return (operand_stack, operator_stack)