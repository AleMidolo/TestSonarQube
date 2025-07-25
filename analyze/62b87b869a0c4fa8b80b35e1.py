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

    if scale is True:
        scale = hist.scale

    bins = hist.bins
    bin_edges = hist.bin_edges
    graph_points = []

    for i, bin_ in enumerate(bins):
        if get_coordinate == "left":
            x = bin_edges[i]
        elif get_coordinate == "right":
            x = bin_edges[i + 1]
        elif get_coordinate == "middle":
            x = (bin_edges[i] + bin_edges[i + 1]) / 2

        value = make_value(bin_)
        if not isinstance(value, (tuple, list)):
            value = (value,)

        if len(value) != len(field_names) - 1:
            raise ValueError("Length of make_value result must match field_names minus one")

        graph_point = (x,) + value
        graph_points.append(graph_point)

    graph = np.array(graph_points, dtype=[(name, 'float64') for name in field_names])
    return graph