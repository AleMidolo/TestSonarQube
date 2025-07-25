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
            if len(expr) == 3:
                op, left, right = expr
                if op == '&':
                    if left == right:
                        return left
                    if isinstance(right, tuple) and len(right) == 3:
                        rop, rleft, rright = right
                        if rop == '|' and rleft == left:
                            return left
                        if rop == '|' and rleft == ('~', left):
                            return (op, left, rright)
                elif op == '|':
                    if left == right:
                        return left
                    if isinstance(right, tuple) and len(right) == 3:
                        rop, rleft, rright = right
                        if rop == '&' and rleft == left:
                            return left
                        if rop == '&' and rleft == ('~', left):
                            return (op, left, rright)
            return (op, apply_absorption(left), apply_absorption(right))
        return expr

    return [apply_absorption(arg) for arg in args]