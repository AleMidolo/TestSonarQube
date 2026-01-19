def compare(self, cur, peek):
    """
        Comparar la precedencia de dos operadores
        :param cur: cadena, el operador actual
        :param peek: cadena, el operador en la parte superior de la pila de operadores
        :return: bool, True si el operador actual tiene una precedencia mayor o igual, False en caso contrario
        >>> expression_calculator = ExpressionCalculator()
        >>> expression_calculator.compare("+", "-")
        True
        """
    cur_index = self.get_priority_index(cur)
    peek_index = self.get_priority_index(peek)
    return self.operat_priority[cur_index] <= self.operat_priority[peek_index]