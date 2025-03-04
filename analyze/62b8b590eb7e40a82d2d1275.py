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
            
        # For each candidate, verify it can be added
        valid_candidates = set()
        for candidate in candidates:
            # Check if candidate appears later in any other list
            valid = True
            positions = element_positions[candidate]
            for ordering, pos in positions:
                if pos > 0 and ordering[pos-1] not in used:
                    valid = False
                    break
            if valid:
                valid_candidates.add(candidate)
                
        if not valid_candidates:
            break
            
        # Add the valid candidates to result
        for candidate in valid_candidates:
            result.append(candidate)
            used.add(candidate)
            # Remove the candidate from all orderings
            for ordering in orderings:
                if ordering and ordering[0] == candidate:
                    ordering.pop(0)
                    
    return result