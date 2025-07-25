def vertex3tuple(vertices):
    """
    Devuelve 3 puntos para cada vértice del polígono. Esto incluirá el vértice y los 2 puntos a ambos lados del vértice.

    Args:
        vertices: Lista de vértices del polígono

    Returns:
        Lista de tuplas, cada una con 3 vértices consecutivos
    """
    result = []
    n = len(vertices)
    
    for i in range(n):
        # Obtiene el vértice anterior (usando módulo para el último vértice)
        prev = vertices[(i - 1) % n]
        # Vértice actual
        curr = vertices[i]
        # Siguiente vértice (usando módulo para el primer vértice)
        next = vertices[(i + 1) % n]
        
        # Agrega la tupla de 3 vértices consecutivos
        result.append((prev, curr, next))
        
    return result