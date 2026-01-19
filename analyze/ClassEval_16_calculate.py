def calculate(self, expression):
    """
    Calcola il valore di un'espressione data
    :param expression: stringa, espressione fornita
    :return: Se ha successo, restituisce il valore dell'espressione; altrimenti, restituisce None
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