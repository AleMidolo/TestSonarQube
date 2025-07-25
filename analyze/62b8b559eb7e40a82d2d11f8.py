def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    if not classes:
        return []
        
    # Remove duplicates while preserving order
    seen = set()
    unique_classes = []
    for cls in classes:
        if cls not in seen:
            seen.add(cls)
            unique_classes.append(cls)
            
    # Remove redundant base classes
    minimal = []
    for i, cls in enumerate(unique_classes):
        is_redundant = False
        for j in range(i + 1, len(unique_classes)):
            # Check if cls is a base class of any later class
            if issubclass(unique_classes[j], cls):
                is_redundant = True
                break
        if not is_redundant:
            minimal.append(cls)
            
    return minimal