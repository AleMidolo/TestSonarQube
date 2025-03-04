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
        
        # Handle single value vs tuple return from make_value
        if isinstance(y, tuple):
            points.append((x,) + y)
        else:
            points.append((x, y))
            
    # Set scale if specified
    if scale is True:
        scale = hist.scale
            
    # Validate field names match point dimensions
    if len(field_names) != len(points[0]):
        raise ValueError(f"Number of field names ({len(field_names)}) must match point dimensions ({len(points[0])})")
        
    # Create and return graph
    from .graph import Graph
    return Graph(points, field_names=field_names, scale=scale)