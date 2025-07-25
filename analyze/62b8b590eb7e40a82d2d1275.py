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
        
    # Create a mapping of element -> list of indices where it appears
    element_positions = {}
    for ordering in orderings:
        for i, element in enumerate(ordering):
            if element not in element_positions:
                element_positions[element] = []
            element_positions[element].append((ordering, i))
            
    result = []
    used = set()
    
    while True:
        # Find elements that can be added (those that appear first in their lists)
        candidates = set()
        for ordering in orderings:
            if ordering:
                element = ordering[0]
                if element not in used:
                    candidates.add(element)
                    
        if not candidates:
            break
            
        # For each candidate, check if it appears later in other lists
        valid_candidates = set()
        for candidate in candidates:
            valid = True
            suffix = None
            
            for pos_list in element_positions[candidate]:
                ordering, idx = pos_list
                if idx > 0 and ordering[0] != candidate:
                    valid = False
                    break
                    
                current_suffix = ordering[idx:]
                if suffix is None:
                    suffix = current_suffix
                elif suffix != current_suffix:
                    valid = False
                    break
                    
            if valid:
                valid_candidates.add(candidate)
                
        if not valid_candidates:
            break
            
        # Add a valid candidate to result and remove from orderings
        element = valid_candidates.pop()
        result.append(element)
        used.add(element)
        
        # Remove the element from the front of any ordering that starts with it
        for ordering in orderings:
            if ordering and ordering[0] == element:
                ordering.pop(0)
                
    return result