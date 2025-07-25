def determineMetaclass(bases, explicit_mc=None):
    """
    Determina la metaclase a partir de una o más clases base y un __metaclass__ explícito opcional.
    """
    metaclasses = []
    
    # Agregar metaclase explícita si existe
    if explicit_mc is not None:
        metaclasses.append(explicit_mc)
    
    # Obtener metaclases de las clases base
    for base in bases:
        if hasattr(base, '__class__'):
            metaclass = type(base)
            if metaclass not in metaclasses:
                metaclasses.append(metaclass)
    
    if not metaclasses:
        return type
    
    # Si solo hay una metaclase, retornarla
    if len(metaclasses) == 1:
        return metaclasses[0]
        
    # Si hay múltiples metaclases, encontrar la más específica
    candidate = metaclasses[0]
    for metaclass in metaclasses[1:]:
        if issubclass(candidate, metaclass):
            continue
        if issubclass(metaclass, candidate):
            candidate = metaclass
        else:
            raise TypeError("Conflicting metaclasses:", candidate, metaclass)
            
    return candidate