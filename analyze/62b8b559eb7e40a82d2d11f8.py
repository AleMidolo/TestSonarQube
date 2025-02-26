def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    from collections import defaultdict

    def find_parent(class_name):
        if class_name not in parent:
            return class_name
        if parent[class_name] != class_name:
            parent[class_name] = find_parent(parent[class_name])
        return parent[class_name]

    parent = {}
    for cls in classes:
        for base in cls.__bases__:
            parent[base.__name__] = cls.__name__

    minimal_classes = set()
    for cls in classes:
        minimal_classes.add(find_parent(cls.__name__))

    return sorted(minimal_classes)