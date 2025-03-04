def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    # Default make_value function returns bin content
    if make_value is None:
        make_value = lambda x: x

    # Get coordinates based on get_coordinate parameter
    if get_coordinate == "left":
        coordinates = [bin.left for bin in hist.bins]
    elif get_coordinate == "right":
        coordinates = [bin.right for bin in hist.bins]
    elif get_coordinate == "middle":
        coordinates = [(bin.left + bin.right)/2 for bin in hist.bins]
    else:
        raise ValueError("get_coordinate must be 'left', 'right' or 'middle'")

    # Create points list
    points = []
    for coord, bin in zip(coordinates, hist.bins):
        value = make_value(bin.content)
        
        # Handle single values vs tuples/lists
        if isinstance(value, (tuple, list)):
            points.append((coord,) + tuple(value))
        else:
            points.append((coord, value))

    # Validate field names match point dimensions
    if len(field_names) != len(points[0]):
        raise ValueError(f"Number of field names ({len(field_names)}) must match point dimensions ({len(points[0])})")

    # Set scale
    if scale is True:
        scale = hist.scale
        
    # Create and return graph
    from .graph import Graph
    return Graph(points, field_names=field_names, scale=scale)