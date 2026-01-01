def calculate(self, expression):
    """
        Calcola il valore di un'espressione data
        :param expression: stringa, espressione fornita
        :return: Se ha successo, restituisce il valore dell'espressione; altrimenti, restituisce None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
    operand_stack = []
    operator_stack = []
    num = ''
    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                operand_stack.append(float(num))
                num = ''
            while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(char):
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            operator_stack.append(char)
    if num:
        operand_stack.append(float(num))
    while operator_stack:
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    return operand_stack[0] if operand_stack else None