def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    from collections import defaultdict

    def find_parent(cls):
        if cls not in parent_map:
            return cls
        root = find_parent(parent_map[cls])
        parent_map[cls] = root
        return root

    parent_map = {}
    for cls in classes:
        for base in cls.__bases__:
            parent_map[base] = cls

    unique_bases = set()
    for cls in classes:
        root = find_parent(cls)
        unique_bases.add(root)

    return sorted(unique_bases, key=lambda x: x.__name__)