def _legacy_mergeOrderings(orderings):
    # Create a dictionary to store item positions
    item_positions = {}
    
    # Create a dictionary to store items that must come before others
    dependencies = {}
    
    # Process each ordering list
    for ordering in orderings:
        # Track position of each item in current ordering
        for i, item in enumerate(ordering):
            # If item seen before, verify suffix matches
            if item in item_positions:
                # Get suffix from current ordering
                curr_suffix = ordering[i:]
                
                # Get suffix from previous ordering
                for prev_ordering in orderings:
                    if item in prev_ordering:
                        prev_i = prev_ordering.index(item)
                        prev_suffix = prev_ordering[prev_i:]
                        
                        # Suffixes must match
                        if curr_suffix != prev_suffix:
                            raise ValueError("Inconsistent orderings")
            
            # Add dependencies - each item must come after previous items
            if i > 0:
                prev = ordering[i-1]
                if item not in dependencies:
                    dependencies[item] = set()
                dependencies[item].add(prev)
                
            # Update position
            item_positions[item] = i
            
    # Build result by processing items with no dependencies first
    result = []
    processed = set()
    
    while item_positions:
        # Find items with no unprocessed dependencies
        available = []
        for item in item_positions:
            if item not in dependencies or \
               all(dep in processed for dep in dependencies[item]):
                available.append(item)
                
        if not available:
            raise ValueError("Circular dependency")
            
        # Add item with lowest position
        next_item = min(available, key=lambda x: item_positions[x])
        result.append(next_item)
        processed.add(next_item)
        del item_positions[next_item]
        
    return result