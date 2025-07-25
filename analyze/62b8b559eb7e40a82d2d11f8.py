def minimalBases(classes):
    """
    Riduce una lista di classi base al suo equivalente minimo ordinato.
    """
    # Create a set to store unique classes
    unique_classes = set()
    
    # Iterate through the list of classes
    for cls in classes:
        # Check if the class is already in the set
        if cls not in unique_classes:
            # Add the class to the set
            unique_classes.add(cls)
    
    # Convert the set back to a sorted list
    return sorted(unique_classes, key=lambda x: x.__name__)