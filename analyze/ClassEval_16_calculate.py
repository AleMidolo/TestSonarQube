def calculate(self, expression):
    """
    Calculate the value of a given expression
    :param expression: string, given expression
    :return:If successful, returns the value of the expression; otherwise, returns None
    >>> calculator = Calculator()
    >>> calculator.calculate('1+2-3')
    0.0
    """
    try:
        # Remove whitespace
        expression = expression.replace(' ', '')
        
        # Check if expression is empty
        if not expression:
            return None
        
        # Validate expression contains only valid characters
        valid_chars = set('0123456789+-*/(). ')
        if not all(c in valid_chars for c in expression):
            return None
        
        # Evaluate the expression
        result = eval(expression)
        
        # Return as float
        return float(result)
    except:
        return None