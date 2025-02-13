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
    return tuple((vertices[i-1], vertices[i], vertices[(i+1) % n]) for i in range(n))