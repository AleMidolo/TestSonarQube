def hist_to_graph(hist, make_value=None, get_coordinate="left", field_names=("x", "y"), scale=None):
    # Default make_value function uses bin content
    if make_value is None:
        make_value = lambda bin_: bin_.value

    # Validate get_coordinate parameter
    valid_coordinates = ["left", "right", "middle"]
    if get_coordinate not in valid_coordinates:
        raise ValueError(f"get_coordinate must be one of {valid_coordinates}")

    # Create points list
    points = []
    for bin_ in hist:
        # Get x coordinate based on get_coordinate parameter
        if get_coordinate == "left":
            x = bin_.left
        elif get_coordinate == "right":
            x = bin_.right
        else:  # middle
            x = (bin_.left + bin_.right) / 2

        # Get y value(s) using make_value function
        y = make_value(bin_)
        
        # Create point tuple with x and y values
        if isinstance(y, tuple):
            points.append((x,) + y)
        else:
            points.append((x, y))

    # Validate field_names length matches point dimensions
    point_dim = len(points[0])
    if len(field_names) != point_dim:
        raise ValueError(f"Number of field names ({len(field_names)}) must match point dimensions ({point_dim})")

    # Create graph with points and field names
    from graph import Graph
    graph = Graph(points=points, field_names=field_names)

    # Set scale if requested
    if scale:
        graph.scale = hist.scale

    return graph