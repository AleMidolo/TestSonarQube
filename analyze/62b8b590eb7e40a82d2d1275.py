def _legacy_mergeOrderings(orderings):
    # Create a dictionary to store the position of each element in its ordering
    position = {}
    for ordering in orderings:
        for i, element in enumerate(ordering):
            if element in position:
                # If element already seen, verify suffix constraint
                old_pos = position[element]
                old_ordering = None
                for o in orderings:
                    if element in o:
                        if old_ordering is None:
                            old_ordering = o[o.index(element):]
                        else:
                            new_ordering = o[o.index(element):]
                            if old_ordering != new_ordering:
                                raise ValueError("Inconsistent orderings")
            else:
                position[element] = i

    # Create graph of dependencies
    graph = {}
    for ordering in orderings:
        for i in range(len(ordering)-1):
            if ordering[i] not in graph:
                graph[ordering[i]] = set()
            graph[ordering[i]].add(ordering[i+1])

    # Topological sort
    result = []
    visited = set()
    temp_mark = set()

    def visit(n):
        if n in temp_mark:
            raise ValueError("Circular dependency detected")
        if n not in visited:
            temp_mark.add(n)
            if n in graph:
                for m in graph[n]:
                    visit(m)
            temp_mark.remove(n)
            visited.add(n)
            result.insert(0, n)

    # Visit all nodes
    nodes = set()
    for ordering in orderings:
        nodes.update(ordering)
    
    for n in nodes:
        if n not in visited:
            visit(n)

    return result[::-1]