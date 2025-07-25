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
    # 如果subjects为空,则所有objects都是根节点
    if not subjects:
        roots.update(objects)
    else:
        # 找出在objects中但不在subjects中的节点,它们就是根节点
        roots.update(objects - subjects)
        
    return roots