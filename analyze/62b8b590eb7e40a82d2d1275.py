def _legacy_mergeOrderings(orderings):
    """
    Combinar múltiples ordenamientos de manera que se preserve el orden dentro de cada uno.

    Los ordenamientos están restringidos de tal forma que, si un objeto aparece en dos o más ordenamientos, entonces el sufijo que comienza con dicho objeto debe estar presente en ambos ordenamientos.

    Por ejemplo:

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

    # Initialize the queue with nodes having zero in-degree
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

    return result