def prepare(self, expression):
    """
        Prepara un'espressione in notazione infissa per la conversione in notazione postfissa.
        :param expression: stringa, l'espressione infissa da preparare
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
            current += c
            i += 1
            continue
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
        else:
            while op_stack and op_stack[-1] != '(' and self.compare(c, op_stack[-1]):
                self.postfix_stack.append(op_stack.pop())
            op_stack.append(c)
        i += 1
    if current:
        self.postfix_stack.append(current)
    while op_stack:
        self.postfix_stack.append(op_stack.pop())