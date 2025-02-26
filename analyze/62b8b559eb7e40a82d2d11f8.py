def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    from collections import defaultdict

    class_graph = defaultdict(set)
    for cls in classes:
        for base in cls.__bases__:
            class_graph[base].add(cls)

    def dfs(cls, visited):
        if cls in visited:
            return set()
        visited.add(cls)
        result = {cls}
        for base in cls.__bases__:
            result.update(dfs(base, visited))
        return result

    minimal_classes = set()
    visited = set()
    for cls in classes:
        if cls not in visited:
            minimal_classes.update(dfs(cls, visited))

    return sorted(minimal_classes, key=lambda x: x.__name__)