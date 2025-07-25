def determineMetaclass(bases, explicit_mc=None):
    """
    从一个或多个基类以及可选的显式 __metaclass__ 中确定元类。
    """
    metaclasses = []
    
    # 收集所有基类的元类
    for base in bases:
        if hasattr(base, '__class__'):
            metaclasses.append(type(base))
    
    # 如果有显式指定的元类,添加到列表中
    if explicit_mc is not None:
        metaclasses.append(explicit_mc)
        
    if not metaclasses:
        return type
        
    # 如果只有一个元类,直接返回
    if len(metaclasses) == 1:
        return metaclasses[0]
        
    # 如果有多个元类,找出最具体的那个
    candidate = metaclasses[0]
    for mc in metaclasses[1:]:
        if issubclass(candidate, mc):
            continue
        if issubclass(mc, candidate):
            candidate = mc
        else:
            raise TypeError("Incompatible metaclasses")
            
    return candidate