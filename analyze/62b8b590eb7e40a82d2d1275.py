def _legacy_mergeOrderings(orderings):
    """
    Merge multiple orderings so that within-ordering order is preserved

    Orderings are constrained in such a way that if an object appears
    in two or more orderings, then the suffix that begins with the
    object must be in both orderings.

    For example:

    >>> _mergeOrderings([
    ... ['x', 'y', 'z'],
    ... ['q', 'z'],
    ... [1, 3, 5],
    ... ['z']
    ... ])
    ['x', 'y', 'q', 1, 3, 5, 'z']
    """
    if not orderings:
        return []
        
    # Create a mapping of elements to their next elements in each ordering
    next_elements = {}
    for ordering in orderings:
        for i in range(len(ordering)-1):
            curr = ordering[i]
            next_elem = ordering[i+1]
            if curr not in next_elements:
                next_elements[curr] = next_elem
            elif next_elements[curr] != next_elem:
                raise ValueError("Inconsistent orderings")

    # Find all elements that are not successors of any other element
    all_elements = set()
    successor_elements = set()
    for ordering in orderings:
        all_elements.update(ordering)
        if len(ordering) > 1:
            successor_elements.update(ordering[1:])
    
    start_elements = all_elements - successor_elements

    # Build the merged ordering
    result = []
    current = list(start_elements)
    seen = set()
    
    while current:
        elem = current.pop(0)
        if elem not in seen:
            result.append(elem)
            seen.add(elem)
            if elem in next_elements:
                current.append(next_elements[elem])
                
    return result