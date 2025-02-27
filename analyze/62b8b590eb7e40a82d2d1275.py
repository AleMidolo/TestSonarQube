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

    # Create a graph and in-degree count
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    orderings_set = set()

    # Build the graph
    for ordering in orderings:
        for i in range(len(ordering)):
            orderings_set.add(ordering[i])
            if i > 0:
                graph[ordering[i - 1]].append(ordering[i])
                in_degree[ordering[i]] += 1

    # Initialize the queue with nodes that have no incoming edges
    queue = deque([item for item in orderings_set if in_degree[item] == 0])
    result = []

    # Perform a topological sort
    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result