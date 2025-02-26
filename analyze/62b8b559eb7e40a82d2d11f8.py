def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    from collections import defaultdict

    def is_subclass(sub, super):
        return issubclass(sub, super)

    # Create a dictionary to hold the base classes
    base_classes = defaultdict(set)

    # Populate the base_classes dictionary
    for cls in classes:
        for base in cls.__bases__:
            base_classes[base].add(cls)

    # Create a list to hold the minimal bases
    minimal_bases = []

    # Check for minimal bases
    for cls in classes:
        if all(not is_subclass(other, cls) for other in minimal_bases):
            minimal_bases.append(cls)

    return minimal_bases