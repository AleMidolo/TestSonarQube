def _legacy_mergeOrderings(orderings):
    # Crear un diccionario para almacenar las posiciones de cada elemento
    positions = {}
    
    # Para cada ordenamiento
    for ordering in orderings:
        # Para cada elemento en el ordenamiento
        for i, element in enumerate(ordering):
            # Si el elemento ya existe en positions
            if element in positions:
                # Verificar que los sufijos coincidan
                suffix1 = ordering[i:]
                suffix2 = orderings[positions[element][0]][positions[element][1]:]
                if suffix1 != suffix2:
                    raise ValueError("Inconsistent orderings")
            else:
                # Almacenar la posición del elemento (índice del ordering, índice del elemento)
                positions[element] = (orderings.index(ordering), i)
    
    # Crear el resultado final
    result = []
    used = set()
    
    # Para cada ordenamiento
    for i, ordering in enumerate(orderings):
        # Para cada elemento en el ordenamiento
        for j, element in enumerate(ordering):
            # Si el elemento no ha sido usado y su primera aparición es en esta posición
            if element not in used and positions[element] == (i, j):
                result.append(element)
                used.add(element)
    
    return result