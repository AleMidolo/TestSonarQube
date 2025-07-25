def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    # 如果没有提供roots参数，初始化一个空集合
    if roots is None:
        roots = set()
    
    # 获取所有作为主语的节点（子节点）
    subjects = set(graph.subjects(prop))
    
    # 获取所有作为宾语的节点（父节点）
    objects = set(graph.objects(prop))
    
    # 根节点是那些作为父节点但不作为子节点的节点
    # 即在objects中但不在subjects中的节点
    roots.update(objects - subjects)
    
    # 如果没有找到根节点，那么所有的主语节点都是根节点
    # 这种情况发生在循环引用或者没有明确的层级结构时
    if not roots:
        roots.update(subjects)
    
    return roots