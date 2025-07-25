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
            
    # Create field names based on number of values
    if len(points[0]) != len(field_names):
        raise ValueError("Number of field names must match number of values per point")
        
    # Import Graph class and create new graph
    from .graph import Graph
    return Graph(points, field_names=field_names, scale=scale)