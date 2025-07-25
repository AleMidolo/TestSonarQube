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
        if isinstance(y, tuple):
            points.append((x,) + y)
        else:
            points.append((x, y))

    # Determine field names based on points structure
    if points and len(points[0]) != len(field_names):
        raise ValueError("Number of field names must match point dimension")

    # Create graph with appropriate scale
    if scale is True:
        scale = hist.scale
        
    from .graph import Graph
    return Graph(points, field_names=field_names, scale=scale)