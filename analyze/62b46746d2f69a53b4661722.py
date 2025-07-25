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
            if expr[0] == '&':
                if isinstance(expr[1], tuple) and expr[1][0] == '|':
                    if expr[1][1] == expr[2]:
                        return expr[2]
                    elif expr[1][2] == expr[2]:
                        return expr[2]
                elif isinstance(expr[2], tuple) and expr[2][0] == '|':
                    if expr[2][1] == expr[1]:
                        return expr[1]
                    elif expr[2][2] == expr[1]:
                        return expr[1]
            elif expr[0] == '|':
                if isinstance(expr[1], tuple) and expr[1][0] == '&':
                    if expr[1][1] == expr[2]:
                        return expr[2]
                    elif expr[1][2] == expr[2]:
                        return expr[2]
                elif isinstance(expr[2], tuple) and expr[2][0] == '&':
                    if expr[2][1] == expr[1]:
                        return expr[1]
                    elif expr[2][2] == expr[1]:
                        return expr[1]
        return expr

    def apply_negative_absorption(expr):
        if isinstance(expr, tuple):
            if expr[0] == '&':
                if isinstance(expr[1], tuple) and expr[1][0] == '|':
                    if isinstance(expr[1][1], tuple) and expr[1][1][0] == '~' and expr[1][1][1] == expr[2]:
                        return ('&', expr[2], expr[1][2])
                    elif isinstance(expr[1][2], tuple) and expr[1][2][0] == '~' and expr[1][2][1] == expr[2]:
                        return ('&', expr[2], expr[1][1])
                elif isinstance(expr[2], tuple) and expr[2][0] == '|':
                    if isinstance(expr[2][1], tuple) and expr[2][1][0] == '~' and expr[2][1][1] == expr[1]:
                        return ('&', expr[1], expr[2][2])
                    elif isinstance(expr[2][2], tuple) and expr[2][2][0] == '~' and expr[2][2][1] == expr[1]:
                        return ('&', expr[1], expr[2][1])
            elif expr[0] == '|':
                if isinstance(expr[1], tuple) and expr[1][0] == '&':
                    if isinstance(expr[1][1], tuple) and expr[1][1][0] == '~' and expr[1][1][1] == expr[2]:
                        return ('|', expr[2], expr[1][2])
                    elif isinstance(expr[1][2], tuple) and expr[1][2][0] == '~' and expr[1][2][1] == expr[2]:
                        return ('|', expr[2], expr[1][1])
                elif isinstance(expr[2], tuple) and expr[2][0] == '&':
                    if isinstance(expr[2][1], tuple) and expr[2][1][0] == '~' and expr[2][1][1] == expr[1]:
                        return ('|', expr[1], expr[2][2])
                    elif isinstance(expr[2][2], tuple) and expr[2][2][0] == '~' and expr[2][2][1] == expr[1]:
                        return ('|', expr[1], expr[2][1])
        return expr

    new_args = []
    for expr in args:
        expr = apply_absorption(expr)
        expr = apply_negative_absorption(expr)
        new_args.append(expr)
    return new_args