def _legacy_mergeOrderings(orderings):
    # Create a dictionary to store the position of each element in its ordering
    position = {}
    for ordering in orderings:
        for i, element in enumerate(ordering):
            if element in position:
                # If element already seen, verify suffix constraint
                old_pos = position[element]
                old_ordering = next(ord for ord in orderings if element in ord and ord.index(element) == old_pos)
                new_ordering = ordering
                
                old_suffix = old_ordering[old_pos:]
                new_suffix = new_ordering[i:]
                
                if old_suffix != new_suffix:
                    raise ValueError("Suffix constraint violated")
            else:
                position[element] = i

    # Create result list by merging orderings
    result = []
    used = set()
    
    # Keep going until we've used all elements
    while len(used) < sum(len(ord) for ord in orderings):
        # Find next unused element that has no unused predecessors
        for ordering in orderings:
            for element in ordering:
                if element in used:
                    continue
                    
                # Check if all predecessors in this ordering are used
                predecessors = ordering[:ordering.index(element)]
                if all(p in used for p in predecessors):
                    result.append(element)
                    used.add(element)
                    break
            else:
                continue
            break
            
    return result