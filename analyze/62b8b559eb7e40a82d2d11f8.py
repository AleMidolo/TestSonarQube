def minimalBases(classes):
    # Create a set to store minimal bases
    minimal = set()
    
    # Iterate through each class
    for c in classes:
        # Check if class is already covered by another base class
        if not any(issubclass(c, other) for other in minimal if other is not c):
            # Remove any classes that are subclasses of current class
            minimal = {m for m in minimal if not issubclass(m, c)}
            # Add current class to minimal set
            minimal.add(c)
            
    # Convert set to sorted list and return
    return sorted(minimal, key=lambda x: x.__name__)