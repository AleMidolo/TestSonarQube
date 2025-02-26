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
        left = vertices[i - 1]  # Previous vertex (wrap around)
        center = vertices[i]     # Current vertex
        right = vertices[(i + 1) % n]  # Next vertex (wrap around)
        result.append((left, center, right))
    return result