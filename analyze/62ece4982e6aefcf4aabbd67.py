def vertex3tuple(vertices):
    # Create list to store 3-tuples
    tuples = []
    
    # Get number of vertices
    n = len(vertices)
    
    # For each vertex
    for i in range(n):
        # Get previous vertex (wrap around to end if at start)
        prev = vertices[(i-1) % n]
        
        # Get current vertex
        curr = vertices[i]
        
        # Get next vertex (wrap around to start if at end) 
        next = vertices[(i+1) % n]
        
        # Add tuple of (prev, curr, next)
        tuples.append(prev + curr + next)
        
    return tuples