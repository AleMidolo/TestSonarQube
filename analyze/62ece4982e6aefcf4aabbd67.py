def vertex3tuple(vertices):
    # Create list to store 3-vertex tuples
    vertex_tuples = []
    
    # Get number of vertices
    n = len(vertices)
    
    # For each vertex index
    for i in range(n):
        # Get previous vertex (wrap around to end if at start)
        prev = vertices[(i-1) % n]
        # Get current vertex
        curr = vertices[i]
        # Get next vertex (wrap around to start if at end) 
        next = vertices[(i+1) % n]
        
        # Add tuple of (previous, current, next) vertices
        vertex_tuples.append((prev, curr, next))
        
    return vertex_tuples