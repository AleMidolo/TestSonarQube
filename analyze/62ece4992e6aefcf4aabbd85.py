def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    # 如果没有提供roots参数，初始化一个空集合
    if roots is None:
        roots = set()
    
    # 获取所有作为主语的节点(子节点)
    subjects = set(graph.subjects(prop))
    
    # 获取所有作为宾语的节点(父节点) 
    objects = set(graph.objects(None, prop))
    
    # 根节点是那些作为宾语出现但不作为主语出现的节点
    # 即没有父节点的节点
    roots.update(objects - subjects)
    
    # 如果没有找到根节点，则所有主语节点都是根节点
    if not roots and subjects:
        roots.update(subjects)
        
    return roots