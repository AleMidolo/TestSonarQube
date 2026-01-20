def prepare(self, expression):
    """
    Prepara la expresión en notación infija para su conversión a notación postfija
    :param expression: cadena, la expresión infija que se va a preparar
    >>> expression_calculator = ExpressionCalculator()
    >>> expression_calculator.prepare("2+3*4")

    expression_calculator.postfix_stack = ['2', '3', '4', '*', '+']
    """
    # Definir precedencia de operadores
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    
    # Pila para operadores
    operator_stack = []
    # Lista para la expresión postfija
    self.postfix_stack = []
    
    # Eliminar espacios en blanco
    expression = expression.replace(' ', '')
    
    i = 0
    while i < len(expression):
        char = expression[i]
        
        # Si es un dígito o punto decimal, extraer el número completo
        if char.isdigit() or char == '.':
            num = ''
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            self.postfix_stack.append(num)
            continue
        
        # Si es paréntesis izquierdo
        elif char == '(':
            operator_stack.append(char)
        
        # Si es paréntesis derecho
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                self.postfix_stack.append(operator_stack.pop())
            if operator_stack:
                operator_stack.pop()  # Eliminar '('
        
        # Si es un operador
        elif char in precedence:
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   operator_stack[-1] in precedence and
                   precedence[operator_stack[-1]] >= precedence[char]):
                self.postfix_stack.append(operator_stack.pop())
            operator_stack.append(char)
        
        i += 1
    
    # Vaciar la pila de operadores
    while operator_stack:
        self.postfix_stack.append(operator_stack.pop())