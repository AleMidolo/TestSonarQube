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

    # Create a graph to track dependencies
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    seen = set()

    # Build the graph
    for ordering in orderings:
        for i in range(len(ordering)):
            if ordering[i] not in seen:
                seen.add(ordering[i])
                if i > 0:
                    graph[ordering[i - 1]].append(ordering[i])
                    in_degree[ordering[i]] += 1
                if ordering[i] not in in_degree:
                    in_degree[ordering[i]] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([item for item in in_degree if in_degree[item] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result