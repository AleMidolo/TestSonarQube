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
    
    # 根节点是那些作为宾语出现但不作为主语出现的节点
    # 以及作为主语出现但其宾语不在图中的节点
    new_roots = objects - subjects
    orphan_subjects = subjects - set(s for s in subjects if any(graph.objects(s, prop)))
    
    # 合并结果
    roots.update(new_roots)
    roots.update(orphan_subjects)
    
    return roots