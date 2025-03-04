def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    # 如果没有提供roots参数,初始化一个空集合
    if roots is None:
        roots = set()
    
    # 获取所有作为主语(child)的节点
    subjects = set(graph.subjects(prop))
    
    # 获取所有作为宾语(parent)的节点 
    objects = set(graph.objects(None, prop))
    
    # 根节点是那些作为宾语但不作为主语的节点
    # 即没有父节点的节点
    new_roots = objects - subjects
    
    # 如果提供了roots参数,将新找到的根节点添加到roots中
    if roots:
        roots.update(new_roots)
        return roots
    
    # 否则直接返回新找到的根节点集合
    return new_roots