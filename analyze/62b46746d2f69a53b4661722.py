def absorb(self, args):
    result = []
    for arg in args:
        # Check if arg is an AND or OR operation
        if hasattr(arg, 'op'):
            # Get operands
            operands = arg.args
            
            # Handle absorption for AND operation
            if arg.op == '&':
                # Check A & (A | B) pattern
                for op in operands:
                    if hasattr(op, 'op') and op.op == '|':
                        if any(a == op.args[0] for a in operands):
                            result.append(op.args[0])
                            break
                        elif any(a == op.args[1] for a in operands):
                            result.append(op.args[1]) 
                            break
                # Check A & (~A | B) pattern (negative absorption)
                for op in operands:
                    if hasattr(op, 'op') and op.op == '|':
                        if any(a == ~op.args[0] for a in operands):
                            result.append(operands[0] & op.args[1])
                            break
                        elif any(a == ~op.args[1] for a in operands):
                            result.append(operands[0] & op.args[0])
                            break
                            
            # Handle absorption for OR operation            
            elif arg.op == '|':
                # Check A | (A & B) pattern
                for op in operands:
                    if hasattr(op, 'op') and op.op == '&':
                        if any(a == op.args[0] for a in operands):
                            result.append(op.args[0])
                            break
                        elif any(a == op.args[1] for a in operands):
                            result.append(op.args[1])
                            break
                # Check A | (~A & B) pattern (negative absorption)
                for op in operands:
                    if hasattr(op, 'op') and op.op == '&':
                        if any(a == ~op.args[0] for a in operands):
                            result.append(operands[0] | op.args[1])
                            break
                        elif any(a == ~op.args[1] for a in operands):
                            result.append(operands[0] | op.args[0])
                            break
            
            # If no absorption pattern found, keep original expression
            if not result:
                result.append(arg)
        else:
            # Not an operation, keep original expression
            result.append(arg)
            
    return result