def vertex3tuple(vertices):
    # Create list to store 3-tuples
    result = []
    
    # Get length of vertices list
    n = len(vertices)
    
    # For each vertex, get previous, current and next vertex
    for i in range(n):
        prev = vertices[(i-1) % n]  # Previous vertex (wraps around)
        curr = vertices[i]          # Current vertex
        next = vertices[(i+1) % n]  # Next vertex (wraps around)
        
        # Add tuple of (prev, curr, next) vertices
        result.append((prev, curr, next))
        
    return result