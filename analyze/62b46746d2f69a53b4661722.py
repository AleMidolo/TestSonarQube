def absorb(self, args):
    """
    Dato un insieme `args` di espressioni, restituisce una nuova lista di espressioni applicando l'assorbimento e l'assorbimento negativo.

    Consulta https://en.wikipedia.org/wiki/Absorption_law

    Assorbimento::

        A & (A | B) = A, A | (A & B) = A

    Assorbimento negativo::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    new_args = []
    for expr in args:
        if isinstance(expr, tuple):
            if expr[0] == '&':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '|':
                    if B[1] == A:
                        new_args.append(A)
                        continue
                    elif isinstance(B[1], tuple) and B[1][0] == '~' and B[1][1] == A:
                        new_args.append(('&', A, B[2]))
                        continue
            elif expr[0] == '|':
                A, B = expr[1], expr[2]
                if isinstance(B, tuple) and B[0] == '&':
                    if B[1] == A:
                        new_args.append(A)
                        continue
                    elif isinstance(B[1], tuple) and B[1][0] == '~' and B[1][1] == A:
                        new_args.append(('|', A, B[2]))
                        continue
        new_args.append(expr)
    return new_args