@staticmethod
def transform(expression):
    """
        Trasforma l'espressione in notazione infissa in un formato adatto per la conversione
        :param expression: stringa, l'espressione infissa da trasformare
        :return: stringa, l'espressione trasformata
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.transform("2 + 3 * 4")
        "2+3*4"
        """
    expression = re.sub('\\s+', '', expression)
    transformed = []
    i = 0
    while i < len(expression):
        c = expression[i]
        if c == '-':
            if i == 0 or expression[i - 1] in '+-*/%(':
                transformed.append('~')
            else:
                transformed.append(c)
        else:
            transformed.append(c)
        i += 1
    return ''.join(transformed)