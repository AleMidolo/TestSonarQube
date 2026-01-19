def calculate(self, expression):
    """
        Calcula el valor de una expresión dada
        :param expression: cadena, expresión dada
        :return: Si tiene éxito, devuelve el valor de la expresión; de lo contrario, devuelve None
        >>> calculator = Calculator()
        >>> calculator.calculate('1+2-3')
        0.0
        """
    operand_stack = []
    operator_stack = []
    i = 0
    while i < len(expression):
        char = expression[i]
        if char.isdigit():
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operand_stack.append(num)
            continue
        elif char in self.operators:
            while operator_stack and self.precedence(operator_stack[-1]) >= self.precedence(char):
                operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
            operator_stack.append(char)
        i += 1
    while operator_stack:
        operand_stack, operator_stack = self.apply_operator(operand_stack, operator_stack)
    return operand_stack[0] if operand_stack else None