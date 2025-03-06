def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    # Create a list to store the minimal bases
    minimal_bases = []
    
    # Iterate through each class in the input list
    for cls in classes:
        # Check if the class is already in the minimal_bases list
        if cls not in minimal_bases:
            # Check if the class is a subclass of any class in the minimal_bases list
            is_subclass = False
            for base in minimal_bases:
                if issubclass(cls, base):
                    is_subclass = True
                    break
            # If the class is not a subclass of any class in the minimal_bases list, add it
            if not is_subclass:
                minimal_bases.append(cls)
    
    # Return the minimal bases list
    return minimal_bases