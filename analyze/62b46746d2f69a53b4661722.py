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
                    return A
                elif isinstance(B, tuple) and B[0] == '|' and isinstance(B[1], tuple) and B[1][0] == '~' and B[1][1] == A:
                    return ('&', A, B[2])
            elif expr[0] == '|':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '&' and B[1] == A:
                    return A
                elif isinstance(B, tuple) and B[0] == '&' and isinstance(B[1], tuple) and B[1][0] == '~' and B[1][1] == A:
                    return ('|', A, B[2])
        return expr

    new_args = []
    for expr in args:
        new_expr = apply_absorption(expr)
        new_args.append(new_expr)
    return new_args