def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    # Default make_value function just returns bin content
    if make_value is None:
        make_value = lambda x: x

    # Get coordinate function based on parameter
    if get_coordinate == "left":
        get_coord = lambda bin: bin.left
    elif get_coordinate == "right":
        get_coord = lambda bin: bin.right
    elif get_coordinate == "middle":
        get_coord = lambda bin: (bin.left + bin.right) / 2
    else:
        raise ValueError("get_coordinate must be 'left', 'right' or 'middle'")

    # Create points list
    points = []
    for bin in hist:
        x = get_coord(bin)
        y = make_value(bin.content)
        
        # Handle both single values and tuples returned by make_value
        if isinstance(y, (tuple, list)):
            points.append((x,) + tuple(y))
        else:
            points.append((x, y))

    # Validate field names match point dimensions
    point_dim = len(points[0])
    if len(field_names) != point_dim:
        raise ValueError(f"Number of field names ({len(field_names)}) must match point dimension ({point_dim})")

    # Create graph with appropriate scale
    from .graph import Graph
    graph = Graph(points, field_names=field_names)
    
    if scale is True:
        graph.scale = hist.scale
    elif scale is not None:
        graph.scale = scale

    return graph