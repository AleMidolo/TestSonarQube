@staticmethod
def transform(expression):
    """
        Transformar la expresión en notación infija a un formato adecuado para la conversión
        :param expression: cadena, la expresión en notación infija a ser transformada
        :return: cadena, la expresión transformada
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"

        """
    expression = re.sub('\\s+', '', expression)
    transformed = []
    i = 0
    length = len(expression)
    while i < length:
        c = expression[i]
        if c == '-':
            if i == 0:
                transformed.append('~')
            elif expression[i - 1] in '+-*/(%':
                transformed.append('~')
            else:
                transformed.append(c)
        else:
            transformed.append(c)
        i += 1
    return ''.join(transformed)