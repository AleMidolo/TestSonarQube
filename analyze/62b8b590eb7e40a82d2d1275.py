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

    # Create a graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph
    for ordering in orderings:
        for i in range(len(ordering)):
            if i > 0:
                graph[ordering[i - 1]].append(ordering[i])
                in_degree[ordering[i]] += 1
            if ordering[i] not in in_degree:
                in_degree[ordering[i]] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([item for item in in_degree if in_degree[item] == 0])
    merged_order = []

    while queue:
        current = queue.popleft()
        merged_order.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return merged_order