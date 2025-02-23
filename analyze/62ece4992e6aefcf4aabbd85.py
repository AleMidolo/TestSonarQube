def find_roots(
    graph: "Graph", prop: "URIRef", roots: Optional[Set["Node"]] = None
) -> Set["Node"]:
    """
    在某种传递层级结构中查找根节点。
    `find_roots(graph, rdflib.RDFS.subClassOf)` 将返回子类层级结构中所有根节点的集合。
    假设三元组的形式为 `(child, prop, parent)`，例如 `RDFS.subClassOf` 或 `SKOS.broader` 的方向。

    参数：
        graph: 图类对象
        prop: URIRef 类对象
        roots: 可选参数，类型为集合（set）

    返回值：
        roots: 包含节点的集合
    """
    if roots is None:
        roots = set()

    all_children = {child for child, _, _ in graph.triples((None, prop, None))}
    all_parents = {parent for _, _, parent in graph.triples((None, prop, None))}

    # 根节点是没有父节点的节点
    root_candidates = all_children - all_parents

    roots.update(root_candidates)
    return roots