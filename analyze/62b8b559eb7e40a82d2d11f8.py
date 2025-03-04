def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    # Create result list to store minimal bases
    result = []
    
    # Iterate through each class in input list
    for c in classes:
        # Check if class should be included
        should_include = True
        
        # Compare against classes already in result
        for r in result:
            # Skip if class is a base class of one already included
            if issubclass(r, c):
                should_include = False
                break
            # Remove existing class if new class is more specific
            elif issubclass(c, r):
                result.remove(r)
        
        # Add class if it should be included
        if should_include:
            result.append(c)
            
    return result