def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Convert a histogram to a graph.

    Args:
        hist: The histogram to convert.
        make_value: A function that sets the value of the graph point.
                    Defaults to the bin content.
        get_coordinate: Defines the coordinate of the graph point from the histogram bin.
                        Can be "left", "right", or "middle".
        field_names: The field names for the graph. Should match the dimensions of the result.
        scale: The scale of the graph. If True, uses the histogram's scale.

    Returns:
        The resulting graph.
    """
    import numpy as np

    if make_value is None:
        make_value = lambda bin_: bin_.content

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

    # Apply make_value to each bin
    values = [make_value(bin_) for bin_ in bin_contents]

    # Create the graph
    graph = np.array(list(zip(x_coords, *values)))

    # Set field names
    if len(field_names) != graph.shape[1]:
        raise ValueError("Number of field names must match the dimensions of the result")

    # Set scale if provided
    if scale is True:
        scale = hist.scale

    return graph, field_names, scale