def prepare(self, expression):
    """
        Prepara la expresión en notación infija para su conversión a notación postfija
        :param expression: cadena, la expresión infija que se va a preparar
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.prepare("2+3*4")

        expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
        """
    op_stack = deque()
    self.postfix_stack.clear()
    arr = list(expression)
    i = 0
    n = len(arr)
    while i < n:
        c = arr[i]
        if c == ' ':
            i += 1
            continue
        if not self.is_operator(c):
            if c == '~':
                i += 1
                if i < n and arr[i].isdigit():
                    num = '-'
                    while i < n and (arr[i].isdigit() or arr[i] == '.'):
                        num += arr[i]
                        i += 1
                    self.postfix_stack.append(num)
                    continue
            else:
                num = ''
                while i < n and (arr[i].isdigit() or arr[i] == '.'):
                    num += arr[i]
                    i += 1
                self.postfix_stack.append(num)
                continue
        else:
            if c == '(':
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