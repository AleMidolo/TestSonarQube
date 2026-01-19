def prepare(self, expression):
    """
        Prepara la expresión en notación infija para su conversión a notación postfija
        :param expression: cadena, la expresión infija que se va a preparar
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    operator_stack = deque()
    self.postfix_stack.clear()
    i = 0
    while i < len(expression):
        c = expression[i]
        if c == ' ':
            i += 1
            continue
        if not self.is_operator(c):
            if c == '~':
                num = '-'
                i += 1
                while i < len(expression) and (not self.is_operator(expression[i])) and (expression[i] != ' '):
                    num += expression[i]
                    i += 1
                self.postfix_stack.append(num)
                continue
            else:
                num = c
                i += 1
                while i < len(expression) and (not self.is_operator(expression[i])) and (expression[i] != ' '):
                    num += expression[i]
                    i += 1
                self.postfix_stack.append(num)
                continue
        if c == '(':
            operator_stack.append(c)
        elif c == ')':
            while operator_stack and operator_stack[-1] != '(':
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.pop()
        else:
            while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.append(c)
        i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())