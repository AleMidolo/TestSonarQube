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
    
    # 根节点是那些作为宾语出现但不作为主语出现的节点
    # 即没有父节点的节点
    new_roots = objects - subjects
    
    # 如果没有找到新的根节点,且subjects非空
    # 则将所有主语节点作为根节点(处理循环引用的情况)
    if not new_roots and subjects:
        new_roots = subjects
        
    # 将新找到的根节点添加到结果集合中
    roots.update(new_roots)
    
    return roots