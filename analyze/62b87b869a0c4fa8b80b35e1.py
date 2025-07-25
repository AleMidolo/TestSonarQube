def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    
    # Default make_value function just returns bin content
    if make_value is None:
        make_value = lambda x: x
        
    # Get coordinate mapping functions
    coordinate_funcs = {
        "left": lambda bin_: bin_.edges[0],
        "right": lambda bin_: bin_.edges[1], 
        "middle": lambda bin_: (bin_.edges[0] + bin_.edges[1])/2
    }
    
    get_coord = coordinate_funcs[get_coordinate]
    
    # Create points list
    points = []
    for bin_ in hist:
        x = get_coord(bin_)
        y = make_value(bin_.value)
        
        # Handle single values vs tuples
        if isinstance(y, tuple):
            points.append((x,) + y)
        else:
            points.append((x, y))
            
    # Set scale if requested
    if scale is True:
        scale = hist.scale
            
    # Create field names based on y value dimensions
    if len(points) > 0 and len(points[0]) > 2:
        # Extend field names if y returns multiple values
        base_names = list(field_names)
        while len(base_names) < len(points[0]):
            base_names.append(f"{field_names[1]}_{len(base_names)-1}")
        field_names = tuple(base_names)
        
    # Create and return graph
    from .graph import Graph
    return Graph(points, field_names=field_names, scale=scale)