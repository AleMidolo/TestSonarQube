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
    i = 0
    while i < len(arr):
        current_char = arr[i]
        if self.is_operator(current_char):
            if count > 0:
                self.postfix_stack.append(''.join(arr[current_index:current_index + count]))
                count = 0
            if current_char == '(':
                op_stack.append(current_char)
            elif current_char == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and op_stack[-1] != '(' and self.compare(current_char, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(current_char)
            current_index = i + 1
        else:
            count += 1
        i += 1
    if count > 0:
        self.postfix_stack.append(''.join(arr[current_index:current_index + count]))
    while op_stack:
        self.postfix_stack.append(op_stack.pop())