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
    operator = operator_stack.pop()
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    result = self.operators[operator](left_operand, right_operand)
    operand_stack.append(result)
    return (operand_stack, operator_stack)