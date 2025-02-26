def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    from collections import defaultdict

    def find_parent(class_name):
        for base in classes[class_name]:
            if base in minimal_classes:
                return minimal_classes[base]
            parent = find_parent(base)
            if parent:
                return parent
        return class_name

    minimal_classes = {}
    for cls in classes:
        minimal_classes[cls] = find_parent(cls)

    return list(dict.fromkeys(minimal_classes.values()))