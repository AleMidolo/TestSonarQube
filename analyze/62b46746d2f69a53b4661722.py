def absorb(self, args):
    """
    Dada una secuencia `args` de expresiones, devuelve una nueva lista de expresiones aplicando absorción y absorción negativa.

    Consulta https://es.wikipedia.org/wiki/Leyes_de_absorci%C3%B3n

    Absorción::

        A & (A | B) = A, A | (A & B) = A

    Absorción negativa::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    def apply_absorption(expr):
        if isinstance(expr, tuple):
            if expr[0] == '&':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '|':
                    if A == B[1]:
                        return A
                    elif A == ('~', B[1]):
                        return ('&', A, B[2])
                elif isinstance(B, tuple) and B[0] == '&':
                    if A == B[1]:
                        return A
                    elif A == ('~', B[1]):
                        return ('&', A, B[2])
            elif expr[0] == '|':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '&':
                    if A == B[1]:
                        return A
                    elif A == ('~', B[1]):
                        return ('|', A, B[2])
                elif isinstance(B, tuple) and B[0] == '|':
                    if A == B[1]:
                        return A
                    elif A == ('~', B[1]):
                        return ('|', A, B[2])
        return expr

    return [apply_absorption(arg) for arg in args]