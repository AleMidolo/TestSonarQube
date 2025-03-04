def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    # 如果没有提供roots参数，初始化一个空集合
    if roots is None:
        roots = set()
    
    # 获取所有作为主语(subject)的节点
    subjects = set(graph.subjects(prop))
    
    # 获取所有作为宾语(object)的节点 
    objects = set(graph.objects(None, prop))
    
    # 根节点是那些作为宾语但不作为主语的节点
    # 也就是说,它们没有父节点
    new_roots = objects - subjects
    
    # 如果没有找到新的根节点,返回所有作为主语的节点
    # 这种情况发生在循环依赖的情况下
    if not new_roots:
        roots.update(subjects)
    else:
        roots.update(new_roots)
        
    return roots