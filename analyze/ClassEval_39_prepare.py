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
    current_index = 0
    count = 0
    current_op = ''
    while current_index < len(arr):
        c = arr[current_index]
        current_index += 1
        if c.isdigit():
            if count > 1:
                current_op = self.postfix_stack.pop() + c
            else:
                current_op = c
            self.postfix_stack.append(current_op)
            count += 1
        else:
            count = 0
            if c == ')':
                while op_stack:
                    op = op_stack.pop()
                    if op == '(':
                        break
                    else:
                        self.postfix_stack.append(op)
            elif not op_stack:
                op_stack.append(c)
            elif c == '(':
                op_stack.append(c)
            else:
                while op_stack and op_stack[-1] != '(' and self.compare(c, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(c)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())