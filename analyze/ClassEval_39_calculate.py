def calculate(self, expression):
    """
    Calculate the result of the given postfix expression
    :param expression: string, the postfix expression to be calculated
    :return: float, the calculated result
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.calculate("2 + 3 * 4")
    14.0

    """
    # Note: The docstring says "postfix" but the example shows infix notation
    # Based on the example, implementing infix expression evaluation
    
    def precedence(op):
        if op in ['+', '-']:
            return 1
        if op in ['*', '/']:
            return 2
        return 0
    
    def apply_operator(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)
    
    operators = []
    values = []
    i = 0
    
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        
        # If current character is a number
        if expression[i].isdigit() or expression[i] == '.':
            num_str = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            values.append(float(num_str))
            continue
        
        # If current character is an opening parenthesis
        elif expression[i] == '(':
            operators.append(expression[i])
        
        # If current character is a closing parenthesis
        elif expression[i] == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # Remove '('
        
        # If current character is an operator
        elif expression[i] in ['+', '-', '*', '/']:
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(expression[i])):
                apply_operator(operators, values)
            operators.append(expression[i])
        
        i += 1
    
    # Apply remaining operators
    while operators:
        apply_operator(operators, values)
    
    return values[0]