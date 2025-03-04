def vertex3tuple(vertices):
    # Create list to store 3-tuples
    result = []
    
    # Get length of vertices list
    n = len(vertices)
    
    # Iterate through each vertex
    for i in range(n):
        # Get previous vertex (wrap around to end if at start)
        prev = vertices[(i-1) % n]
        # Get current vertex
        curr = vertices[i]
        # Get next vertex (wrap around to start if at end) 
        next = vertices[(i+1) % n]
        
        # Add tuple of (prev, curr, next) vertices
        result.append((prev, curr, next))
        
    return result