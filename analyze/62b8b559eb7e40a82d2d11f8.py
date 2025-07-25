def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    if not classes:
        return []
        
    # Create result list starting with first class
    result = [classes[0]]
    
    # Check each subsequent class
    for c in classes[1:]:
        # Check if class is already covered by a superclass
        redundant = False
        for r in result:
            if issubclass(r, c):
                redundant = True
                break
            # Replace any classes that this class covers
            elif issubclass(c, r):
                result[result.index(r)] = c
                redundant = True
                break
                
        # Add non-redundant classes
        if not redundant:
            result.append(c)
            
    return result