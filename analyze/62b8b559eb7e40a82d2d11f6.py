def determineMetaclass(bases, explicit_mc=None):
    if explicit_mc is not None:
        return explicit_mc
    metaclasses = [type(base) for base in bases]
    return max(metaclasses, key=lambda m: m.__mro__.index(m))