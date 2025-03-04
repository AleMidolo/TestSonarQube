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
        
    # Create a set of all elements
    all_elements = set()
    for ordering in orderings:
        all_elements.update(ordering)
    
    # Create a dictionary mapping each element to its successors in each ordering
    successors = {elem: set() for elem in all_elements}
    for ordering in orderings:
        for i in range(len(ordering)-1):
            successors[ordering[i]].add(ordering[i+1])
            
    # Create a set of elements with no predecessors
    no_predecessors = set(all_elements)
    for succ_set in successors.values():
        no_predecessors.difference_update(succ_set)
        
    # Build the merged ordering
    result = []
    used = set()
    
    while no_predecessors:
        # Take any element with no predecessors
        elem = no_predecessors.pop()
        result.append(elem)
        used.add(elem)
        
        # Update no_predecessors set
        # Check if any successor of elem now has no unused predecessors
        if elem in successors:
            for succ in successors[elem]:
                if succ not in used:
                    # Check if all predecessors of succ are used
                    all_preds_used = True
                    for ordering in orderings:
                        if succ in ordering:
                            idx = ordering.index(succ)
                            if any(pred not in used for pred in ordering[:idx]):
                                all_preds_used = False
                                break
                    if all_preds_used:
                        no_predecessors.add(succ)
    
    return result