def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent
    """
    # Create a set to track classes that can be removed
    redundant = set()
    
    # Compare each class with all classes that come after it
    for i, base in enumerate(classes):
        for other in classes[i + 1:]:
            # If base is a subclass of other, other is redundant
            if issubclass(base, other):
                redundant.add(other)
            # If other is a subclass of base, base is redundant    
            elif issubclass(other, base):
                redundant.add(base)
                
    # Return list of classes with redundant ones removed, maintaining original order
    return [c for c in classes if c not in redundant]