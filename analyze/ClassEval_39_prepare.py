def prepare(self, expression):
    """
        Prepara un'espressione in notazione infissa per la conversione in notazione postfissa.
        :param expression: stringa, l'espressione infissa da preparare
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    operator_stack = deque()
    self.postfix_stack.clear()
    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isdigit() or c == '.' or c == '~':
            num_str = ''
            if c == '~':
                num_str += '-'
                i += 1
                if i < len(expression):
                    c = expression[i]
            while i < len(expression) and (c.isdigit() or c == '.'):
                num_str += c
                i += 1
                if i < len(expression):
                    c = expression[i]
            self.postfix_stack.append(num_str)
            continue
        elif self.is_operator(c):
            if c == '(':
                operator_stack.append(c)
            elif c == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.postfix_stack.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()
            else:
                while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(c)
        i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())