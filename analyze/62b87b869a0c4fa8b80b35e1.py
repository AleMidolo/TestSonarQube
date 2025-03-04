def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    # Default make_value function just returns bin content
    if make_value is None:
        make_value = lambda x: x
        
    # Validate get_coordinate parameter
    valid_coords = ["left", "right", "middle"]
    if get_coordinate not in valid_coords:
        raise ValueError(f"get_coordinate must be one of {valid_coords}")
        
    # Get coordinate based on specified position
    def get_bin_coordinate(bin):
        if get_coordinate == "left":
            return bin.left_edge
        elif get_coordinate == "right":
            return bin.right_edge
        else:  # middle
            return (bin.left_edge + bin.right_edge) / 2
            
    # Create points list
    points = []
    for bin in hist:
        x = get_bin_coordinate(bin)
        y = make_value(bin.value)
        
        # Handle single values vs tuples from make_value
        if isinstance(y, (tuple, list)):
            points.append((x,) + tuple(y))
        else:
            points.append((x, y))
            
    # Validate field names match point dimensions
    point_len = len(points[0]) if points else 0
    if len(field_names) != point_len:
        raise ValueError(f"Number of field names ({len(field_names)}) must match point dimensions ({point_len})")
        
    # Create graph with specified parameters
    from graph import Graph  # Assuming Graph class exists
    graph = Graph(points=points, field_names=field_names)
    
    # Set scale if specified
    if scale is True:
        graph.scale = hist.scale
    elif scale is not None:
        graph.scale = scale
        
    return graph