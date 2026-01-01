def prepare(self, expression):
    """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
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
            operator_stack.pop()
        elif self.is_operator(c):
            while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.append(c)
        else:
            operand = []
            while i < len(expression) and (not self.is_operator(expression[i])):
                operand.append(expression[i])
                i += 1
            self.postfix_stack.append(''.join(operand))
            i -= 1
        i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())