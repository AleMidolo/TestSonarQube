def vertex3tuple(vertices):
    """
    Restituisce 3 punti per ogni vertice del poligono. Questo includerà il vertice e i 2 punti su entrambi i lati del vertice::

    Esempio:  
    Poligono con vertici ABCD  
    Restituirà:  
    DAB, ABC, BCD, CDA -> restituisce tuple di 3 elementi  
    #A    B    C    D  -> dei vertici
    """
    n = len(vertices)
    result = []
    for i in range(n):
        # Calcola gli indici per i punti precedenti e successivi
        prev_index = (i - 1) % n
        next_index = (i + 1) % n
        # Crea la tupla con i 3 punti
        triplet = (vertices[prev_index], vertices[i], vertices[next_index])
        result.append(triplet)
    return result