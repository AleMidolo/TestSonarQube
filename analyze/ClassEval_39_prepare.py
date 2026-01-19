def prepare(self, expression):
    """
        准备中缀表达式以便转换为后缀表示法
        :param expression: 字符串，要准备的中缀表达式
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")
        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    arr = list(expression)
    current_index = 0
    count = 0
    current_token = ''
    while current_index < len(arr):
        c = arr[current_index]
        current_index += 1
        if not self.is_operator(c):
            if c != '~' and (not c.isdigit()) and (c != '.'):
                raise ValueError('Invalid character in expression: {}'.format(c))
            current_token += c
            if current_index >= len(arr):
                self.postfix_stack.append(current_token)
            else:
                next_char = arr[current_index]
                if self.is_operator(next_char) or next_char == '~':
                    self.postfix_stack.append(current_token)
                    current_token = ''
        else:
            if len(current_token) > 0:
                self.postfix_stack.append(current_token)
                current_token = ''
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
    if len(current_token) > 0:
        self.postfix_stack.append(current_token)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())