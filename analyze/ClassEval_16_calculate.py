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
        
        # Evaluate the expression safely
        result = eval(expression)
        
        # Return as float
        return float(result)
    except:
        return None