def calculate(self, expression):
    """
    Calcular el resultado de la expresión en notación postfija dada
    :param expression: cadena, la expresión en notación postfija a calcular
    :return: float, el resultado calculado
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.calculate("2 + 3 * 4")
    14.0

    """
    # Convert infix to postfix first, then evaluate
    postfix = self._infix_to_postfix(expression)
    return self._evaluate_postfix(postfix)

def _infix_to_postfix(self, expression):
    """Convert infix expression to postfix notation"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operator_stack = []
    
    tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
    
    for token in tokens:
        if token.replace('.', '').replace('-', '').isdigit():
            output.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # Remove '('
        elif token in precedence:
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[token]):
                output.append(operator_stack.pop())
            operator_stack.append(token)
    
    while operator_stack:
        output.append(operator_stack.pop())
    
    return output

def _evaluate_postfix(self, postfix):
    """Evaluate postfix expression"""
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
    
    return float(stack[0])