def minimalBases(classes):
    """
    Riduce una lista di classi base al suo equivalente minimo ordinato.
    """
    # Create a set to store unique classes
    unique_classes = set()
    
    # Iterate through the list of classes
    for cls in classes:
        # Check if the class is already in the set
        if not any(issubclass(cls, existing_cls) for existing_cls in unique_classes):
            # Remove any existing classes that are subclasses of the current class
            unique_classes = {existing_cls for existing_cls in unique_classes if not issubclass(existing_cls, cls)}
            # Add the current class to the set
            unique_classes.add(cls)
    
    # Return the sorted list of unique classes
    return sorted(unique_classes, key=lambda x: x.__name__)