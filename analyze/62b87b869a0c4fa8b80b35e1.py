def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    # Default make_value function returns bin content
    if make_value is None:
        make_value = lambda x: x
        
    # Get coordinates based on get_coordinate parameter
    if get_coordinate == "left":
        coordinates = [bin.left for bin in hist.bins()]
    elif get_coordinate == "right":
        coordinates = [bin.right for bin in hist.bins()]
    elif get_coordinate == "middle":
        coordinates = [(bin.left + bin.right)/2 for bin in hist.bins()]
    else:
        raise ValueError("get_coordinate must be 'left', 'right' or 'middle'")
        
    # Get values using make_value function
    values = [make_value(bin.content) for bin in hist.bins()]
    
    # Handle single values vs tuples
    if not isinstance(values[0], tuple):
        values = [(v,) for v in values]
        
    # Create points list
    points = []
    for coord, val in zip(coordinates, values):
        point = (coord,) + val
        points.append(point)
        
    # Set scale
    if scale is True:
        scale = hist.scale
        
    # Create and return graph with given field names and points
    from .graph import Graph
    return Graph(field_names=field_names, points=points, scale=scale)