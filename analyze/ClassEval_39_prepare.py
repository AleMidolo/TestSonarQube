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
        if c == '(':
            operator_stack.append(c)
        elif c == ')':
            while operator_stack and operator_stack[-1] != '(':
                self.postfix_stack.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()
        elif self.is_operator(c):
            if c == '-' and (i == 0 or expression[i - 1] in '+-*/(\\~'):
                c = '~'
            if c == '~':
                j = i + 1
                if j < len(expression) and expression[j] == '(':
                    self.postfix_stack.append('0')
                    operator_stack.append('-')
                else:
                    num_start = j
                    while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                        j += 1
                    num = expression[num_start:j]
                    self.postfix_stack.append('~' + num)
                    i = j - 1
            else:
                while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(c)
        else:
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            num = expression[i:j]
            self.postfix_stack.append(num)
            i = j - 1
        i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())