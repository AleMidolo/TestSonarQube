def minimalBases(classes):
    """
    Reduce una lista de clases base a su equivalente mínimo ordenado.
    """
    minimal = []
    for cls in sorted(classes, key=lambda x: x.__name__):
        if not any(issubclass(cls, base) for base in minimal):
            minimal.append(cls)
    return tuple(minimal)