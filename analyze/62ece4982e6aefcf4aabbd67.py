def vertex3tuple(vertices):
    '''
    Restituisce 3 punti per ogni vertice del poligono. Questo includerà il vertice e i 2 punti su entrambi i lati del vertice::

    Esempio:  
    Poligono con vertici ABCD  
    Restituirà:  
    DAB, ABC, BCD, CDA -> restituisce tuple di 3 elementi  
    #A    B    C    D  -> dei vertici
    '''
    n = len(vertices)
    result = []
    for i in range(n):
        left = vertices[i - 1]  # il vertice a sinistra
        center = vertices[i]     # il vertice corrente
        right = vertices[(i + 1) % n]  # il vertice a destra, con wrap-around
        result.append((left, center, right))
    return result