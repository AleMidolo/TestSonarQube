def minimalBases(classes):
    """
    Reduce a list of base classes to its ordered minimum equivalent.
    
    Args:
        classes (list): A list of base classes.
    
    Returns:
        list: A list of base classes that is the minimal equivalent of the input list.
    """
    minimal = []
    for cls in classes:
        if not any(issubclass(cls, base) for base in minimal):
            minimal.append(cls)
    return minimal