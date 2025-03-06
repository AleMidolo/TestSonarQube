def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    minimal = []
    for cls in classes:
        if not any(issubclass(cls, base) for base in minimal):
            minimal.append(cls)
    return minimal