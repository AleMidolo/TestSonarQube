def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    from collections import defaultdict

    def is_subclass(sub, super):
        return issubclass(sub, super)

    # Create a graph of subclasses
    graph = defaultdict(set)
    for cls in classes:
        for other_cls in classes:
            if cls != other_cls and is_subclass(cls, other_cls):
                graph[other_cls].add(cls)

    # Perform a topological sort to find the minimal bases
    visited = set()
    result = []

    def dfs(cls):
        if cls in visited:
            return
        visited.add(cls)
        for neighbor in graph[cls]:
            dfs(neighbor)
        result.append(cls)

    for cls in classes:
        dfs(cls)

    # Reverse the result to get the ordered minimum equivalent
    return result[::-1]