def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Convert a histogram to a graph.

    Parameters:
    - hist: The histogram to convert.
    - make_value: Function to set the value of a graph point. Defaults to bin content.
    - get_coordinate: Determines the coordinate of a graph point. Can be "left", "right", or "middle".
    - field_names: Names of the graph fields. Must match the result dimension.
    - scale: Scale of the graph. If True, uses the histogram's scale.

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

    # Calculate coordinates based on get_coordinate
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

    # Create the graph data
    graph_data = {field_names[0]: x_coords}
    for i in range(len(y_values[0])):
        graph_data[field_names[i + 1]] = [y[i] for y in y_values]

    # Handle scale
    if scale is True:
        scale = hist.scale

    # Return the graph (assuming a Graph class exists)
    return Graph(data=graph_data, scale=scale)