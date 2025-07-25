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

    # Create a graph to represent the orderings
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Build the graph and in-degree count
    for ordering in orderings:
        for i in range(len(ordering)):
            if i > 0:
                graph[ordering[i - 1]].append(ordering[i])
                in_degree[ordering[i]] += 1
            if ordering[i] not in in_degree:
                in_degree[ordering[i]] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    merged_order = []

    while queue:
        node = queue.popleft()
        merged_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return merged_order