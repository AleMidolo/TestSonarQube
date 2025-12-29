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
        if c.isdigit() or c == '.' or c == '~' or (c in 'Ee' and i > 0 and (arr[i - 1].isdigit() or arr[i - 1] == '.')):
            if c == '~':
                current += '-'
            else:
                current += c
            if i + 1 < len(arr):
                next_c = arr[i + 1]
                if next_c.isdigit() or next_c == '.' or next_c in 'Ee' or (next_c in '+-' and arr[i] in 'Ee'):
                    i += 1
                    continue
            self.postfix_stack.append(current)
            current = ''
        else:
            if current:
                self.postfix_stack.append(current)
                current = ''
            if c == '(':
                op_stack.append(c)
            elif c == ')':
                while op_stack and op_stack[-1] != '(':
                    self.postfix_stack.append(op_stack.pop())
                if op_stack:
                    op_stack.pop()
            elif self.is_operator(c):
                while op_stack and op_stack[-1] != '(' and self.compare(c, op_stack[-1]):
                    self.postfix_stack.append(op_stack.pop())
                op_stack.append(c)
        i += 1
    if current:
        self.postfix_stack.append(current)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())