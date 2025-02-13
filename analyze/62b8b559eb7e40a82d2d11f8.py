def minimalBases(classes):
    return [cls for cls in classes if not any(issubclass(subclass, cls) for subclass in classes if subclass is not cls)]