def absorb(self, args):
    """
    Given an `args` sequence of expressions, return a new list of expression
    applying absorption and negative absorption.

    See https://en.wikipedia.org/wiki/Absorption_law

    Absorption::

        A & (A | B) = A, A | (A & B) = A

    Negative absorption::

        A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    def apply_absorption(expr):
        if isinstance(expr, tuple):
            if len(expr) == 3:
                op, left, right = expr
                if op == '&':
                    if left == right:
                        return left
                    if isinstance(right, tuple) and right[0] == '|' and right[1] == left:
                        return left
                    if isinstance(right, tuple) and right[0] == '|' and right[1] == ('~', left):
                        return (op, left, right[2])
                elif op == '|':
                    if left == right:
                        return left
                    if isinstance(right, tuple) and right[0] == '&' and right[1] == left:
                        return left
                    if isinstance(right, tuple) and right[0] == '&' and right[1] == ('~', left):
                        return (op, left, right[2])
            return (op, apply_absorption(left), apply_absorption(right))
        return expr

    return [apply_absorption(arg) for arg in args]