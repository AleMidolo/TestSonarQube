def _legacy_mergeOrderings(orderings):
    # Create a dictionary to store item positions
    item_positions = {}
    
    # Create a dictionary to store items that must come before others
    dependencies = {}
    
    # Process each ordering list
    for ordering in orderings:
        # Track position of each item in this ordering
        for i, item in enumerate(ordering):
            if item not in item_positions:
                item_positions[item] = []
            item_positions[item].append(i)
            
            # Add dependencies - each item must come after previous items
            if i > 0:
                prev = ordering[i-1]
                if prev not in dependencies:
                    dependencies[prev] = set()
                dependencies[prev].add(item)
                
    # Get all unique items
    all_items = set()
    for ordering in orderings:
        all_items.update(ordering)
        
    # Build result by taking items with no dependencies first
    result = []
    while all_items:
        # Find items with no dependencies
        available = set()
        for item in all_items:
            has_deps = False
            for deps in dependencies.values():
                if item in deps:
                    has_deps = True
                    break
            if not has_deps:
                available.add(item)
                
        if not available:
            raise ValueError("Circular dependency detected")
            
        # Take the first available item
        next_item = available.pop()
        result.append(next_item)
        all_items.remove(next_item)
        
        # Remove this item from dependencies
        if next_item in dependencies:
            del dependencies[next_item]
            
    return result