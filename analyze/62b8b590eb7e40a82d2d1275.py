def _legacy_mergeOrderings(orderings):
    """
    将多个列表按出现顺序合并为一个不包含重复元素的列表。
    合并多个排序列表（orderings），同时保留每个排序列表中的顺序。

    这些排序列表受到以下约束：如果某个对象出现在两个或多个排序列表中，那么以该对象为起点的后缀部分必须在所有相关的排序列表中一致。

    例如：
    >>> _mergeOrderings([
    ... ['x', 'y', 'z'],
    ... ['q', 'z'],
    ... [1, 3, 5],
    ... ['z']
    ... ])
    ['x', 'y', 'q', 1, 3, 5, 'z']
    """
    from collections import defaultdict, deque

    # 构建图
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    all_nodes = set()

    for ordering in orderings:
        for i in range(len(ordering) - 1):
            u, v = ordering[i], ordering[i + 1]
            if v not in graph[u]:
                graph[u].add(v)
                in_degree[v] += 1
            all_nodes.add(u)
            all_nodes.add(v)
        if ordering:
            all_nodes.add(ordering[-1])

    # 拓扑排序
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return result