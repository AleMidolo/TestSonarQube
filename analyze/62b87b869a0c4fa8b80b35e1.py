def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    # Default make_value function returns bin content
    if make_value is None:
        make_value = lambda x: x

    # Get coordinates based on specified method
    def get_bin_coordinate(bin):
        if get_coordinate == "left":
            return bin.left
        elif get_coordinate == "right":
            return bin.right
        elif get_coordinate == "middle":
            return (bin.left + bin.right) / 2
        else:
            raise ValueError("get_coordinate must be 'left', 'right' or 'middle'")

    # Create points list
    points = []
    for bin in hist:
        x = get_bin_coordinate(bin)
        y = make_value(bin.content)
        
        # Handle both single values and tuples from make_value
        if isinstance(y, (tuple, list)):
            points.append((x,) + tuple(y))
        else:
            points.append((x, y))

    # Create graph with appropriate dimensions
    from graph import Graph
    sample_point = points[0]
    dimensions = len(sample_point)
    
    # Verify field_names matches dimensions
    if len(field_names) != dimensions:
        raise ValueError(f"Number of field names ({len(field_names)}) must match point dimensions ({dimensions})")
    
    # Create graph
    graph = Graph(dimensions=dimensions, field_names=field_names)
    
    # Add points to graph
    for point in points:
        graph.add_point(*point)
        
    # Set scale if specified
    if scale is True:
        graph.scale = hist.scale
    elif scale is not None:
        graph.scale = scale
        
    return graph