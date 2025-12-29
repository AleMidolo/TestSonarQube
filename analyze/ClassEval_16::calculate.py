def calculate(self, expression):
    """
        Calcola il valore di un'espressione data
        :param expression: stringa, espressione fornita
        :return: Se ha successo, restituisce il valore dell'espressione; altrimenti, restituisce None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
    if not expression:
        return None
    expression = expression.replace(' ', '')
    if not expression:
        return None
    operand_stack = []
    operator_stack = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit() or (expression[i] == '.' and i + 1 < len(expression) and expression[i + 1].isdigit()):
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            try:
                num = float(expression[i:j])
                operand_stack.append(num)
            except ValueError:
                return None
            i = j
        elif expression[i] in self.operators:
            while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(expression[i]):
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            operator_stack.append(expression[i])
            i += 1
        else:
            return None
    while operator_stack:
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    if len(operand_stack) == 1:
        return operand_stack[0]
    else:
        return None