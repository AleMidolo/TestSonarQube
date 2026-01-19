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
        if expression[i].isdigit() or expression[i] == '.':
            j = i
            while j < n and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            try:
                operand_stack.append(float(expression[i:j]))
            except ValueError:
                return None
            i = j
        elif expression[i] in self.operators:
            while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(expression[i]):
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            operator_stack.append(expression[i])
            i += 1
        elif expression[i] == ' ':
            i += 1
        else:
            return None
    while operator_stack:
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    if len(operand_stack) == 1 and (not operator_stack):
        return operand_stack[0]
    else:
        return None