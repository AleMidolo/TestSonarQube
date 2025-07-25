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

    # Create a graph and a count of incoming edges
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    orderings_set = set()

    for ordering in orderings:
        for i in range(len(ordering)):
            orderings_set.add(ordering[i])
            if i > 0:
                if ordering[i] not in graph[ordering[i - 1]]:
                    graph[ordering[i - 1]].add(ordering[i])
                    in_degree[ordering[i]] += 1

    # Initialize the queue with nodes that have no incoming edges
    queue = deque([item for item in orderings_set if in_degree[item] == 0])
    merged_order = []

    while queue:
        current = queue.popleft()
        merged_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return merged_order