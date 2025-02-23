def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    from collections import defaultdict

    def find_parent(class_name):
        if class_name not in parent:
            return class_name
        root = find_parent(parent[class_name])
        parent[class_name] = root  # Path compression
        return root

    parent = {}
    for cls in classes:
        for base in cls.__bases__:
            parent[base.__name__] = cls.__name__

    unique_bases = set()
    for cls in classes:
        root = find_parent(cls.__name__)
        unique_bases.add(root)

    return list(unique_bases)