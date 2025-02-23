def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    from collections import defaultdict

    class_graph = defaultdict(set)
    for cls in classes:
        for base in cls.__bases__:
            class_graph[base].add(cls)

    def find_minimal_bases(cls, visited):
        if cls in visited:
            return set()
        visited.add(cls)
        minimal_bases = {cls}
        for base in cls.__bases__:
            minimal_bases.update(find_minimal_bases(base, visited))
        return minimal_bases

    minimal_classes = set()
    visited = set()
    for cls in classes:
        minimal_classes.update(find_minimal_bases(cls, visited))

    return sorted(minimal_classes, key=lambda x: x.__name__)