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

    # Create a graph to represent the orderings
    graph = defaultdict(set)
    in_degree = defaultdict(int)
    all_items = set()

    # Build the graph and in-degree count
    for ordering in orderings:
        for i in range(len(ordering)):
            all_items.add(ordering[i])
            if i < len(ordering) - 1:
                if ordering[i + 1] not in graph[ordering[i]]:
                    graph[ordering[i]].add(ordering[i + 1])
                    in_degree[ordering[i + 1]] += 1
                if ordering[i] not in in_degree:
                    in_degree[ordering[i]] = 0

    # Topological sort using Kahn's algorithm
    queue = deque([item for item in all_items if in_degree[item] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return result