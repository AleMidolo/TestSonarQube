def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    from collections import defaultdict

    def find_parent(class_name):
        if class_name not in parent:
            return class_name
        root = find_parent(parent[class_name])
        parent[class_name] = root
        return root

    parent = {}
    for cls in classes:
        for base in cls[1:]:
            root_cls = find_parent(cls[0])
            root_base = find_parent(base)
            if root_cls != root_base:
                parent[root_base] = root_cls

    unique_bases = set(find_parent(cls[0]) for cls in classes)
    return sorted(unique_bases)