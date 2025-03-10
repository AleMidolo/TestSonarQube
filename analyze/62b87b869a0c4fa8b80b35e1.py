def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Convert a histogram to a graph.

    Parameters:
    - hist: The histogram to convert.
    - make_value: Function to set the value of a graph point. Defaults to bin content.
    - get_coordinate: Determines the coordinate of a graph point. Can be "left", "right", or "middle".
    - field_names: Names of the graph fields. Must match the result dimension.
    - scale: The scale of the graph. If True, uses the histogram's scale.

    Returns:
    - The resulting graph.
    """
    import numpy as np

    if make_value is None:
        make_value = lambda bin_: bin_

    if get_coordinate not in ["left", "right", "middle"]:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    # Extract bin edges and contents
    bin_edges = hist.bin_edges
    bin_contents = hist.bin_contents

    # Determine the x-coordinates based on get_coordinate
    if get_coordinate == "left":
        x_coords = bin_edges[:-1]
    elif get_coordinate == "right":
        x_coords = bin_edges[1:]
    elif get_coordinate == "middle":
        x_coords = (bin_edges[:-1] + bin_edges[1:]) / 2

    # Apply make_value to each bin content
    y_values = [make_value(bin_) for bin_ in bin_contents]

    # Ensure y_values is a list of tuples or lists
    if not all(isinstance(y, (tuple, list)) for y in y_values):
        y_values = [(y,) for y in y_values]

    # Check if field_names match the dimension of y_values
    if len(field_names) != len(y_values[0]) + 1:
        raise ValueError("field_names must match the dimension of the result")

    # Create the graph
    graph = []
    for x, y in zip(x_coords, y_values):
        point = {"x": x}
        for i, field in enumerate(field_names[1:]):
            point[field] = y[i]
        graph.append(point)

    # Set the scale if provided
    if scale is True:
        scale = hist.scale
    elif scale is None:
        scale = "unknown"

    return graph, scale