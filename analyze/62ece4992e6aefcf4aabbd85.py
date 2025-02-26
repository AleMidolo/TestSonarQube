from typing import Optional, Set
from rdflib import Graph, URIRef

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set["Node"]] = None
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

    # Find all nodes that have parents
    children_with_parents = {child for child, _, parent in graph.triples((None, prop, None))}

    # Find all nodes that are parents
    parents = {parent for _, _, parent in graph.triples((None, prop, None))}

    # Roots are those nodes that are not parents of any other nodes
    roots = {child for child in children_with_parents if child not in parents}

    return roots