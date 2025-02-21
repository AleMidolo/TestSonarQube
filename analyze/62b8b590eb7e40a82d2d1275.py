def _legacy_mergeOrderings(orderings):
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