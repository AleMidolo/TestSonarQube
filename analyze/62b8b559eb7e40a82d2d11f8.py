def minimalBases(classes):
    """
    आधार कक्षाओं (base classes) की सूची को उसके क्रमबद्ध न्यूनतम समकक्ष (ordered minimum equivalent) में घटाएं।
    """
    from collections import defaultdict

    def is_subclass(sub, super):
        return issubclass(sub, super)

    minimal_classes = []
    for cls in classes:
        if not any(is_subclass(cls, min_cls) for min_cls in minimal_classes):
            minimal_classes = [min_cls for min_cls in minimal_classes if not is_subclass(min_cls, cls)]
            minimal_classes.append(cls)

    return minimal_classes