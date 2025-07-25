def _legacy_mergeOrderings(orderings):
    # Create a dictionary to store the position of each element in its ordering
    position = {}
    for ordering in orderings:
        for i, element in enumerate(ordering):
            if element in position:
                # Check that suffixes match when element appears in multiple orderings
                suffix1 = ordering[i:]
                suffix2 = orderings[position[element][0]][position[element][1]:]
                if suffix1 != suffix2:
                    raise ValueError(f"Inconsistent orderings for element {element}")
            else:
                position[element] = (orderings.index(ordering), i)
    
    # Create result list by merging orderings
    result = []
    used = set()
    
    # Process each ordering
    for ordering in orderings:
        # Add elements from this ordering that haven't been used yet
        for element in ordering:
            if element not in used:
                result.append(element)
                used.add(element)
                
    return result