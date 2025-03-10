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
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_nodes = set()

    for ordering in orderings:
        for i in range(len(ordering) - 1):
            u, v = ordering[i], ordering[i + 1]
            if v not in graph[u]:
                graph[u].append(v)
                in_degree[v] += 1
            all_nodes.add(u)
            all_nodes.add(v)

    # Initialize the queue with nodes that have no incoming edges
    queue = deque([node for node in all_nodes if in_degree[node] == 0])
    result = []

    # Perform topological sort
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Check for cycles (if any nodes still have in-degree > 0)
    if len(result) != len(all_nodes):
        raise ValueError("Input orderings contain a cycle or are inconsistent")

    return result