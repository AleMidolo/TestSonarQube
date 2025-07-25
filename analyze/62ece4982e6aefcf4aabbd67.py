def vertex3tuple(vertices):
    """
    Devuelve 3 puntos para cada vértice del polígono. Esto incluirá el vértice y los 2 puntos a ambos lados del vértice.

    Args:
        vertices (list): Lista de vértices del polígono.

    Returns:
        list: Lista de tuplas de 3 elementos, donde cada tupla contiene el vértice y sus dos vecinos.
    """
    n = len(vertices)
    result = []
    for i in range(n):
        # Obtener el vértice actual y sus dos vecinos
        prev_vertex = vertices[(i - 1) % n]
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % n]
        # Crear la tupla de 3 elementos
        result.append((prev_vertex, current_vertex, next_vertex))
    return result