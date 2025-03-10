def _legacy_mergeOrderings(orderings):
    """
    Merge multiple orderings so that within-ordering order is preserved

    Orderings are constrained in such a way that if an object appears
    in two or more orderings, then the suffix that begins with the
    object must be in both orderings.

    For example:

    >>> _mergeOrderings([
    ... ['x', 'y', 'z'],
    ... ['q', 'z'],
    ... [1, 3, 5],
    ... ['z']
    ... ])
    ['x', 'y', 'q', 1, 3, 5, 'z']
    """
    from collections import defaultdict, deque

    # Build a graph and in-degree count
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

    # Initialize queue with nodes having zero in-degree
    queue = deque([node for node in all_nodes if in_degree[node] == 0])

    # Perform topological sort
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return result