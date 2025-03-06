def absorb(self, args):
    """
    Dato un insieme `args` di espressioni, restituisce una nuova lista di espressioni applicando l'assorbimento e l'assorbimento negativo.

    Consulta https://en.wikipedia.org/wiki/Absorption_law

    Assorbimento::

        A & (A | B) = A, A | (A & B) = A

    Assorbimento negativo::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    def apply_absorption(expr):
        if isinstance(expr, tuple):
            if expr[0] == '&':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '|' and B[1] == A:
                    return A  # A & (A | B) = A
                if isinstance(B, tuple) and B[0] == '|' and B[1] == ('~', A):
                    return ('&', A, B[2])  # A & (~A | B) = A & B
            elif expr[0] == '|':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '&' and B[1] == A:
                    return A  # A | (A & B) = A
                if isinstance(B, tuple) and B[0] == '&' and B[1] == ('~', A):
                    return ('|', A, B[2])  # A | (~A & B) = A | B
        return expr

    return [apply_absorption(expr) for expr in args]