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
        if isinstance(expr, tuple) and len(expr) == 2:
            a, b = expr
            if isinstance(a, str) and isinstance(b, str):
                # Apply absorption laws
                if a == f"({a} | {b})":
                    new_expressions.append(a)
                elif a == f"({a} & {b})":
                    new_expressions.append(a)
                elif a == f"({a} & (~{a} | {b}))":
                    new_expressions.append(f"({a} & {b})")
                elif a == f"({a} | (~{a} & {b}))":
                    new_expressions.append(f"({a} | {b})")
                else:
                    new_expressions.append(expr)
            else:
                new_expressions.append(expr)
        else:
            new_expressions.append(expr)
    return new_expressions