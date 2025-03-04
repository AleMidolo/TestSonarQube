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
                
    # Create result list
    result = []
    used = set()
    
    # Helper function to check if an item can be added
    def can_add(item):
        if item in dependencies:
            # Check that all dependencies of this item are already used
            return all(dep in used for dep in dependencies[item])
        return True
        
    # Keep adding items until all are used
    while len(used) < len(item_positions):
        # Find next available item
        for item in item_positions:
            if item not in used and can_add(item):
                result.append(item)
                used.add(item)
                break
                
    return result