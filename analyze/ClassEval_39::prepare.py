def prepare(self, expression):
    """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    operator_stack = deque()
    i = 0
    while i < len(expression):
        c = expression[i]
        if c.isdigit() or c == '~':
            num = c
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '.'):
                i += 1
                num += expression[i]
            self.postfix_stack.append(num)
        elif self.is_operator(c):
            while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.append(c)
        elif c == '(':
            operator_stack.append(c)
        elif c == ')':
            while operator_stack and operator_stack[-1] != '(':
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.pop()
        i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())