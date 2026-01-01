def prepare(self, expression):
    """
        准备中缀表达式以便转换为后缀表示法
        :param expression: 字符串，要准备的中缀表达式
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
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1] == '~'):
                i += 1
                num += expression[i]
            self.postfix_stack.append(num)
        elif c in {'+', '-', '*', '\\/', '%', '(', ')'}:
            if c == '(':
                operator_stack.append(c)
            elif c == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.pop()
            else:
                while operator_stack and operator_stack[-1] != '(' and self.compare(c, operator_stack[-1]):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(c)
        i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())