def absorb(self, args):
    # 创建结果列表
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
                if (expr1.is_and() and expr2.is_or() and 
                    any(t1 == t2 for t1 in expr1.terms for t2 in expr2.terms)):
                    result[j] = expr1
                    changed = True
                    
                # 检查吸收律 A | (A & B) = A  
                elif (expr1.is_or() and expr2.is_and() and
                      any(t1 == t2 for t1 in expr1.terms for t2 in expr2.terms)):
                    result[j] = expr1
                    changed = True
                    
                # 检查负吸收律 A & (~A | B) = A & B
                elif (expr1.is_and() and expr2.is_or() and
                      any(t1.is_not() and t1.term == t2 for t1 in expr2.terms for t2 in expr1.terms)):
                    new_terms = [t for t in expr2.terms if not any(t.is_not() and t.term == t2 for t2 in expr1.terms)]
                    result[j] = expr1 & Expression.make_and(new_terms)
                    changed = True
                    
                # 检查负吸收律 A | (~A & B) = A | B
                elif (expr1.is_or() and expr2.is_and() and
                      any(t1.is_not() and t1.term == t2 for t1 in expr2.terms for t2 in expr1.terms)):
                    new_terms = [t for t in expr2.terms if not any(t.is_not() and t.term == t2 for t2 in expr1.terms)]
                    result[j] = expr1 | Expression.make_or(new_terms)
                    changed = True
                    
    return result