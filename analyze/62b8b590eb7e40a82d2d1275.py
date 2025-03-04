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
    all_items = set(item_positions.keys())
    
    # Initialize result list
    result = []
    
    # Keep track of items we've added
    added = set()
    
    # Helper function to check if an item can be added
    def can_add(item):
        if item in dependencies:
            # Check that all dependencies have been added
            return all(dep in added for dep in dependencies[item])
        return True
        
    # Add items until we've used them all
    while len(result) < len(all_items):
        # Find items that can be added
        available = [item for item in all_items - added if can_add(item)]
        
        if not available:
            raise ValueError("Circular dependency detected")
            
        # Add the first available item
        result.append(available[0])
        added.add(available[0])
        
    return result