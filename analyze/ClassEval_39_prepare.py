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
        token = expression[i]
        if token.isdigit() or (token == '~' and (i + 1 < len(expression) and expression[i + 1].isdigit())):
            num = token
            i += 1
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            self.postfix_stack.append(num)
        elif token in {'+', '-', '*', '\\/', '%', '(', ')'}:
            if token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.pop()
            else:
                while operator_stack and self.compare(token, operator_stack[-1]):
                    self.postfix_stack.append(operator_stack.pop())
                operator_stack.append(token)
            i += 1
        else:
            i += 1
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())