def calculate(self, expression):
    """
        Calcula el valor de una expresión dada
        :param expression: cadena, expresión dada
        :return: Si tiene éxito, devuelve el valor de la expresión; de lo contrario, devuelve None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
    if not expression:
        return None
    operand_stack = []
    operator_stack = []
    i = 0
    n = len(expression)
    while i < n:
        char = expression[i]
        if char.isdigit() or char == '.':
            j = i
            while j < n and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            try:
                num = float(expression[i:j])
            except ValueError:
                return None
            operand_stack.append(num)
            i = j
        elif char in self.operators:
            while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(char):
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            operator_stack.append(char)
            i += 1
        elif char == ' ':
            i += 1
        else:
            return None
    while operator_stack:
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    if len(operand_stack) == 1:
        return operand_stack[0]
    else:
        return None