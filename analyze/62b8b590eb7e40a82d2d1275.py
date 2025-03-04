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
        
    # Create a mapping of elements to their positions in each ordering
    positions = {}
    for ordering in orderings:
        for i, elem in enumerate(ordering):
            if elem not in positions:
                positions[elem] = []
            positions[elem].append(i)
            
    # Create a set of all unique elements
    all_elements = set()
    for ordering in orderings:
        all_elements.update(ordering)
        
    result = []
    used = set()
    
    while len(used) < len(all_elements):
        # Find elements that can be added next
        candidates = []
        for elem in all_elements:
            if elem in used:
                continue
                
            # Check if all elements before this one in each ordering are used
            can_add = True
            for ordering in orderings:
                if elem in ordering:
                    idx = ordering.index(elem)
                    if any(x not in used for x in ordering[:idx]):
                        can_add = False
                        break
                        
            if can_add:
                candidates.append(elem)
                
        # Add the candidate that appears earliest in its orderings
        if not candidates:
            raise ValueError("Circular dependency detected")
            
        best_candidate = min(candidates, key=lambda x: min(positions[x]))
        result.append(best_candidate)
        used.add(best_candidate)
        
    return result