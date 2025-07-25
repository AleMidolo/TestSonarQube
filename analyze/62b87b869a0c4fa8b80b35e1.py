def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    # Default make_value function just returns bin content
    if make_value is None:
        make_value = lambda x: x

    # Validate get_coordinate parameter
    valid_coords = ["left", "right", "middle"]
    if get_coordinate not in valid_coords:
        raise ValueError(f"get_coordinate must be one of {valid_coords}")

    # Create points list
    points = []
    for bin_ in hist:
        # Get x coordinate based on get_coordinate parameter
        if get_coordinate == "left":
            x = bin_.left_edge
        elif get_coordinate == "right":
            x = bin_.right_edge
        else:  # middle
            x = (bin_.left_edge + bin_.right_edge) / 2

        # Get y value(s) using make_value function
        y = make_value(bin_.value)
        
        # If y is a tuple/list, flatten with x coordinate
        if isinstance(y, (tuple, list)):
            point = (x,) + tuple(y)
        else:
            point = (x, y)
            
        points.append(point)

    # Validate field names match point dimensions
    if len(field_names) != len(points[0]):
        raise ValueError(f"Number of field names ({len(field_names)}) must match point dimensions ({len(points[0])})")

    # Create graph with appropriate scale
    from graph import Graph  # Assuming Graph class exists
    graph = Graph(points, field_names=field_names)
    
    if scale is True:
        graph.scale = hist.scale
    elif scale is not None:
        graph.scale = scale

    return graph