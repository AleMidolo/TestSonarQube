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

    # Construir el grafo de dependencias
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

    # Inicializar la cola con nodos que no tienen dependencias
    queue = deque([node for node in all_nodes if in_degree[node] == 0])

    # Realizar el ordenamiento topológico
    result = []
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Verificar si hay un ciclo (lo cual no debería ocurrir según las restricciones)
    if len(result) != len(all_nodes):
        raise ValueError("Existe un ciclo en las dependencias, lo cual no está permitido.")

    return result