def calculate(self, expression):
    """
    Calcula el valor de una expresión dada
    :param expression: cadena, expresión dada
    :return: Si tiene éxito, devuelve el valor de la expresión; de lo contrario, devuelve None
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
        
        # Validate characters in expression
        valid_chars = set('0123456789+-*/(). ')
        if not all(c in valid_chars for c in expression):
            return None
        
        # Evaluate the expression safely
        result = eval(expression)
        
        # Return as float
        return float(result)
    except:
        return None