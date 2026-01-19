def calculate(self, expression):
    """
    Calcola il risultato dell'espressione postfix fornita
    :param expression: stringa, l'espressione postfix da calcolare
    :return: float, il risultato calcolato
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.calculate("2 + 3 * 4")
    14.0

    """
    # Convert infix to postfix first, then evaluate
    def precedence(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0
    
    def infix_to_postfix(expr):
        output = []
        stack = []
        tokens = expr.replace('(', ' ( ').replace(')', ' ) ').split()
        
        for token in tokens:
            if token.replace('.', '').replace('-', '').isdigit():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack:
                    stack.pop()
            elif token in ['+', '-', '*', '/']:
                while stack and stack[-1] != '(' and precedence(stack[-1]) >= precedence(token):
                    output.append(stack.pop())
                stack.append(token)
        
        while stack:
            output.append(stack.pop())
        
        return output
    
    def evaluate_postfix(postfix):
        stack = []
        for token in postfix:
            if token in ['+', '-', '*', '/']:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a / b)
            else:
                stack.append(float(token))
        
        return stack[0]
    
    postfix = infix_to_postfix(expression)
    return evaluate_postfix(postfix)