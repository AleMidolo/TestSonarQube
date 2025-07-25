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
    has_pred = set()
    for succ_set in successors.values():
        has_pred.update(succ_set)
    no_pred = all_elements - has_pred
    
    # Build result list by repeatedly taking elements with no predecessors
    result = []
    while no_pred:
        # Take any element with no predecessors
        elem = no_pred.pop()
        result.append(elem)
        
        # Remove this element from successor sets and update no_pred
        succs = successors[elem]
        del successors[elem]
        
        # Check if removing elem as predecessor creates new elements with no predecessors
        for other_succs in successors.values():
            if elem in other_succs:
                other_succs.remove(elem)
                
        for e in succs:
            if not any(e in s for s in successors.values()):
                no_pred.add(e)
                
    return result