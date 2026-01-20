def prepare(self, expression):
    """
    Prepara la expresión en notación infija para su conversión a notación postfija
    :param expression: cadena, la expresión infija que se va a preparar
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.prepare("2+3*4")

    expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
    """
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Initialize output list and operator stack
    output = []
    operator_stack = []
    
    # Remove whitespace from expression
    expression = expression.replace(' ', '')
    
    # Parse the expression
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # If character is a digit or decimal point, extract the full number
        if char.isdigit() or char == '.':
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            output.append(num)
            continue
        
        # If character is an opening parenthesis
        elif char == '(':
            operator_stack.append(char)
        
        # If character is a closing parenthesis
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                output.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # Remove the '('
        
        # If character is an operator
        elif char in precedence:
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[char]):
                output.append(operator_stack.pop())
            operator_stack.append(char)
        
        i += 1
    
    # Pop remaining operators from stack
    while operator_stack:
        output.append(operator_stack.pop())
    
    # Store result in postfix_stack attribute
    self.postfix_stack = output