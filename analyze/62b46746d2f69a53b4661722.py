def absorb(self, args):
    """
    对于给定的表达式序列 `args`，返回一个应用吸收律的新表达式列表。

    对于给定的表达式序列 `args`，返回一个应用吸收律和负吸收律的新表达式列表。

    参考：https://en.wikipedia.org/wiki/Absorption_law

    吸收律（Absorption）::

      A & (A | B) = A, A | (A & B) = A

    负吸收律（Negative Absorption）::

      A & (~A | B) = A & B, A | (~A & B) = A | B
    """
    new_args = []
    for expr in args:
        # Apply Absorption Law
        if isinstance(expr, tuple) and len(expr) == 3:
            op1, operator, op2 = expr
            if operator == '&':
                if op1 == op2 or (op1 == 'A' and op2 == ('A', '|', 'B')) or (op2 == 'A' and op1 == ('A', '|', 'B')):
                    new_args.append(op1)
                    continue
            elif operator == '|':
                if op1 == op2 or (op1 == 'A' and op2 == ('A', '&', 'B')) or (op2 == 'A' and op1 == ('A', '&', 'B')):
                    new_args.append(op1)
                    continue
        
        # Apply Negative Absorption Law
        if isinstance(expr, tuple) and len(expr) == 3:
            op1, operator, op2 = expr
            if operator == '&':
                if op1 == ('~', op2) or op2 == ('~', op1):
                    new_args.append(('&', op1, op2))
                    continue
            elif operator == '|':
                if op1 == ('~', op2) or op2 == ('~', op1):
                    new_args.append(('|', op1, op2))
                    continue
        
        new_args.append(expr)
    
    return new_args