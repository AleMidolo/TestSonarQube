def _legacy_mergeOrderings(orderings):
    """
    Unisci più ordinamenti in modo che l'ordine all'interno di ciascun ordinamento venga preservato.

    Gli ordinamenti sono vincolati in modo tale che, se un oggetto appare in due o più ordinamenti, il suffisso che inizia con l'oggetto deve essere presente in entrambi gli ordinamenti.

    Ad esempio:

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