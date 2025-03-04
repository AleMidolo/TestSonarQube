def absorb(self, args):
    """
    Dato un insieme `args` di espressioni, restituisce una nuova lista di espressioni applicando l'assorbimento e l'assorbimento negativo.

    Consulta https://en.wikipedia.org/wiki/Absorption_law

    Assorbimento::

        A & (A | B) = A, A | (A & B) = A

    Assorbimento negativo::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    def absorb_expression(expr):
        # Implement absorption laws
        if isinstance(expr, And):
            if isinstance(expr.args[0], Or):
                return expr.args[0].args[0]  # A & (A | B) = A
            elif isinstance(expr.args[1], Or):
                return expr.args[1].args[0]  # A & (A | B) = A
            elif isinstance(expr.args[0], Not) and isinstance(expr.args[1], Or):
                return And(expr.args[0].args[0], expr.args[1].args[1])  # A & (~A | B) = A & B
        elif isinstance(expr, Or):
            if isinstance(expr.args[0], And):
                return expr.args[0].args[0]  # A | (A & B) = A
            elif isinstance(expr.args[1], And):
                return expr.args[1].args[0]  # A | (A & B) = A
            elif isinstance(expr.args[0], Not) and isinstance(expr.args[1], And):
                return Or(expr.args[0].args[0], expr.args[1].args[1])  # A | (~A & B) = A | B
        return expr

    return [absorb_expression(expr) for expr in args]