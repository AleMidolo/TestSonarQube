def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Convert a histogram to a graph.

    Args:
        hist: The histogram to convert.
        make_value: A function that sets the value of the graph point.
                   Defaults to the bin content.
        get_coordinate: Defines the coordinate of the graph point from the histogram bin.
                        Can be "left" (default), "right", or "middle".
        field_names: Sets the field names of the graph. The number of names should match
                     the dimension of the result.
        scale: The scale of the graph. If True, uses the histogram's scale.

    Returns:
        The resulting graph.
    """
    import numpy as np

    if make_value is None:
        make_value = lambda bin_: bin_.content

    if get_coordinate not in ["left", "right", "middle"]:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    # Determine the coordinates based on get_coordinate
    if get_coordinate == "left":
        coordinates = hist.bin_edges[:-1]
    elif get_coordinate == "right":
        coordinates = hist.bin_edges[1:]
    elif get_coordinate == "middle":
        coordinates = (hist.bin_edges[:-1] + hist.bin_edges[1:]) / 2

    # Apply make_value to each bin
    values = [make_value(bin_) for bin_ in hist.bins]

    # Create the graph
    graph = np.array(list(zip(coordinates, *zip(*values))))

    # Set field names
    graph.dtype = [(field_names[0], graph.dtype)] + [(field_names[i], graph.dtype) for i in range(1, len(field_names))]

    # Set scale if provided
    if scale is True:
        graph.scale = hist.scale
    elif scale is not None:
        graph.scale = scale

    return graph