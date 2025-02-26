def absorb(self, args):
    """
    Dato un insieme `args` di espressioni, restituisce una nuova lista di espressioni applicando l'assorbimento e l'assorbimento negativo.

    Consulta https://en.wikipedia.org/wiki/Absorption_law

    Assorbimento::

        A & (A | B) = A, A | (A & B) = A

    Assorbimento negativo::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    new_expressions = []
    for expr in args:
        if isinstance(expr, tuple) and len(expr) == 3:
            A, op, B = expr
            if op == '&':
                if (A == B) or (B == ('|', A)):
                    new_expressions.append(A)
                elif (A == ('~', B)) or (B == ('~', A)):
                    new_expressions.append(('&', A, B))
                else:
                    new_expressions.append(expr)
            elif op == '|':
                if (A == B) or (B == ('&', A)):
                    new_expressions.append(A)
                elif (A == ('~', B)) or (B == ('~', A)):
                    new_expressions.append(('|', A, B))
                else:
                    new_expressions.append(expr)
        else:
            new_expressions.append(expr)
    return new_expressions