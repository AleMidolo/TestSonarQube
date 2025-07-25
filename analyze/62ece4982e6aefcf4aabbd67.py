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
        point1 = vertices[i - 1]  # punto a sinistra
        point2 = vertices[i]      # vertice corrente
        point3 = vertices[(i + 1) % n]  # punto a destra
        result.append((point1, point2, point3))
    return result