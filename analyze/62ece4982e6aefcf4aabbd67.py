def vertex3tuple(vertices):
    """
    Return 3 points for each vertex of the polygon. This will include the vertex and the 2 points on both sides of the vertex.

    :param vertices: List of vertices of the polygon.
    :return: List of 3-tuples representing the vertex and its two adjacent vertices.
    """
    n = len(vertices)
    result = []
    for i in range(n):
        # Get the current vertex and its two adjacent vertices
        prev_vertex = vertices[(i - 1) % n]
        current_vertex = vertices[i]
        next_vertex = vertices[(i + 1) % n]
        # Append the 3-tuple to the result
        result.append((prev_vertex, current_vertex, next_vertex))
    return result