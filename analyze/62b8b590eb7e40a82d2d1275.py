def _legacy_mergeOrderings(orderings):
    # Create a dictionary to store item positions
    item_positions = {}
    
    # Create a dictionary to store items that must come after each item
    must_follow = {}
    
    # Process each ordering
    for ordering in orderings:
        for i, item in enumerate(ordering):
            # Add item to must_follow dict if not already present
            if item not in must_follow:
                must_follow[item] = set()
            
            # Record position of item in this ordering
            if item not in item_positions:
                item_positions[item] = []
            item_positions[item].append(i)
            
            # Add all items that must follow this item
            must_follow[item].update(ordering[i+1:])
    
    # Create result list
    result = []
    used = set()
    
    # Helper function to check if an item can be added
    def can_add(item):
        # Item must not be used already
        if item in used:
            return False
            
        # All items that must come before this item must be used
        for other_item in must_follow:
            if item in must_follow[other_item] and other_item not in used:
                return False
                
        return True
    
    # Keep adding items until all are used
    while len(used) < len(must_follow):
        # Find next available item
        available = None
        for item in must_follow:
            if can_add(item):
                available = item
                break
                
        if available is None:
            raise ValueError("Circular dependency detected")
            
        result.append(available)
        used.add(available)
        
    return result