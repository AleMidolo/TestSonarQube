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
                if (isinstance(expr1, str) and isinstance(expr2, tuple) and 
                    len(expr2) == 3 and expr2[1] == '|' and
                    expr1 == expr2[0]):
                    if expr1 not in result:
                        result.append(expr1)
                        changed = True
                
                # 检查吸收律 A | (A & B) = A        
                if (isinstance(expr1, str) and isinstance(expr2, tuple) and
                    len(expr2) == 3 and expr2[1] == '&' and
                    expr1 == expr2[0]):
                    if expr1 not in result:
                        result.append(expr1)
                        changed = True
                        
                # 检查负吸收律 A & (~A | B) = A & B
                if (isinstance(expr1, str) and isinstance(expr2, tuple) and
                    len(expr2) == 3 and expr2[1] == '|' and
                    isinstance(expr2[0], tuple) and len(expr2[0]) == 2 and
                    expr2[0][0] == '~' and expr2[0][1] == expr1):
                    new_expr = (expr1, '&', expr2[2])
                    if new_expr not in result:
                        result.append(new_expr)
                        changed = True
                        
                # 检查负吸收律 A | (~A & B) = A | B
                if (isinstance(expr1, str) and isinstance(expr2, tuple) and
                    len(expr2) == 3 and expr2[1] == '&' and
                    isinstance(expr2[0], tuple) and len(expr2[0]) == 2 and
                    expr2[0][0] == '~' and expr2[0][1] == expr1):
                    new_expr = (expr1, '|', expr2[2])
                    if new_expr not in result:
                        result.append(new_expr)
                        changed = True
                        
    return result