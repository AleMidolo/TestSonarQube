def prepare(self, expression):
    """
        Prepare the infix expression for conversion to postfix notation
        :param expression: string, the infix expression to be prepared
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")
        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    arr = list(expression)
    current = ''
    count = 0
    for i, c in enumerate(arr):
        if self.is_operator(c):
            if len(current) > 0:
                self.postfix_stack.append(current)
                current = ''
            if c == '(':
                op_stack.append(c)
            elif c == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(' and self.compare(c, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(c)
        else:
            current += c
    if current:
        self.postfix_stack.append(current)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())