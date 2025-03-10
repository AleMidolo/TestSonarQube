def vertex3tuple(vertices):
    """
    Devuelve 3 puntos para cada vértice del polígono. Esto incluirá el vértice y los 2 puntos a ambos lados del vértice::

    un polígono con vértices ABCD:  
    Retornará:  
    DAB, ABC, BCD, CDA -> devuelve tuplas de 3 elementos  
    #A    B    C    D  -> de los vértices
    """
    n = len(vertices)
    result = []
    for i in range(n):
        # Obtener el vértice actual y los dos adyacentes
        prev_index = (i - 1) % n
        current_index = i
        next_index = (i + 1) % n
        
        # Crear la tupla de 3 elementos
        triplet = (vertices[prev_index], vertices[current_index], vertices[next_index])
        result.append(triplet)
    
    return result