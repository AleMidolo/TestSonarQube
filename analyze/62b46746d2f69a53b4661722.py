def absorb(self, args):
    # 初始化结果列表
    result = list(args)
    changed = True
    
    # 持续应用吸收律直到没有变化
    while changed:
        changed = False
        n = len(result)
        
        # 遍历所有表达式对
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                    
                # 获取两个表达式
                expr1 = result[i]
                expr2 = result[j]
                
                # 检查吸收律 A & (A | B) = A
                if (isinstance(expr1, And) and 
                    isinstance(expr2, Or) and
                    expr1 in expr2.args):
                    result[j] = expr1
                    changed = True
                    
                # 检查吸收律 A | (A & B) = A  
                elif (isinstance(expr1, Or) and
                      isinstance(expr2, And) and 
                      expr1 in expr2.args):
                    result[j] = expr1
                    changed = True
                    
                # 检查负吸收律 A & (~A | B) = A & B
                elif (isinstance(expr1, And) and
                      isinstance(expr2, Or) and
                      Not(expr1) in expr2.args):
                    new_args = [arg for arg in expr2.args if arg != Not(expr1)]
                    result[j] = And(expr1, *new_args)
                    changed = True
                    
                # 检查负吸收律 A | (~A & B) = A | B
                elif (isinstance(expr1, Or) and
                      isinstance(expr2, And) and
                      Not(expr1) in expr2.args):
                    new_args = [arg for arg in expr2.args if arg != Not(expr1)]
                    result[j] = Or(expr1, *new_args)
                    changed = True
                    
        # 移除重复项
        result = list(set(result))
                    
    return result