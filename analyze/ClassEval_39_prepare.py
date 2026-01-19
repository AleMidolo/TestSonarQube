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
    current = ''
    i = 0
    while i < len(arr):
        c = arr[i]
        if not self.is_operator(c):
            if c == '~':
                current += '-'
            else:
                current += c
            if i == len(arr) - 1 or self.is_operator(arr[i + 1]):
                if current:
                    self.postfix_stack.append(current)
                    current = ''
        elif c == '(':
            op_stack.append(c)
        elif c == ')':
            while op_stack and op_stack[-1] != '(':
                self.postfix_stack.append(op_stack.pop())
            if op_stack:
                op_stack.pop()
        else:
            while op_stack and op_stack[-1] != '(' and self.compare(c, op_stack[-1]):
                self.postfix_stack.append(op_stack.pop())
            op_stack.append(c)
        i += 1
    while op_stack:
        self.postfix_stack.append(op_stack.pop())