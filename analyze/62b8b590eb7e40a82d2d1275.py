def _legacy_mergeOrderings(orderings):
    """
    कई क्रमबद्ध सूचियों को इस प्रकार संयोजित करें कि प्रत्येक सूची के भीतर का क्रम संरक्षित रहे।

    इन सूचियों पर यह प्रतिबंध है कि यदि कोई वस्तु दो या अधिक सूचियों में प्रकट होती है,
    तो उस वस्तु से शुरू होने वाला उपसर्ग (suffix) सभी सूचियों में समान होना चाहिए।

    उदाहरण के लिए:

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

    # Check for cycles (if any node still has in-degree > 0)
    if len(result) != len(all_nodes):
        raise ValueError("Input orderings contain a cycle or conflicting dependencies.")

    return result