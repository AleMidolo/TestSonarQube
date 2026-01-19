def prepare(self, expression):
    """
    Prepara un'espressione in notazione infissa per la conversione in notazione postfissa.
    :param expression: stringa, l'espressione infissa da preparare
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.prepare("2+3*4")

    expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
    """
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Stack for operators
    operator_stack = []
    # List for postfix expression
    self.postfix_stack = []
    
    # Parse the expression
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # Skip whitespace
        if char == ' ':
            i += 1
            continue
        
        # If character is a digit, extract the full number
        if char.isdigit() or char == '.':
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            self.postfix_stack.append(num)
            continue
        
        # If character is an opening parenthesis
        elif char == '(':
            operator_stack.append(char)
        
        # If character is a closing parenthesis
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                self.postfix_stack.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # Remove the '('
        
        # If character is an operator
        elif char in precedence:
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[char]):
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.append(char)
        
        i += 1
    
    # Pop all remaining operators
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())