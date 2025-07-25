from typing import Set, Optional
from rdflib import Graph, URIRef, Node

def find_roots(
    graph: Graph, prop: URIRef, roots: Optional[Set[Node]] = None
) -> Set[Node]:
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
    
    # 获取所有作为子节点的节点
    children = set(graph.subjects(prop, None))
    
    # 获取所有作为父节点的节点
    parents = set(graph.objects(None, prop))
    
    # 根节点是没有父节点的节点
    roots.update(parents - children)
    
    return roots