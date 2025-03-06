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
        field_names: Sets the field names of the graph. The number should match the dimension of the result.
        scale: The scale of the graph. If True, uses the histogram's scale.

    Returns:
        The resulting graph.
    """
    import numpy as np

    if make_value is None:
        make_value = lambda bin_: bin_.content

    if get_coordinate not in ["left", "right", "middle"]:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    if scale is None:
        scale = hist.scale if hasattr(hist, 'scale') else None

    bins = hist.bins
    x_coords = []
    y_values = []

    for bin_ in bins:
        if get_coordinate == "left":
            x_coord = bin_.left_edge
        elif get_coordinate == "right":
            x_coord = bin_.right_edge
        elif get_coordinate == "middle":
            x_coord = (bin_.left_edge + bin_.right_edge) / 2

        x_coords.append(x_coord)
        y_values.append(make_value(bin_))

    graph = np.recarray(len(x_coords), dtype=[(field_names[0], 'f8')] + [(name, 'f8') for name in field_names[1:]])
    graph[field_names[0]] = x_coords
    for i, name in enumerate(field_names[1:]):
        graph[name] = [y[i] for y in y_values]

    if scale is not None:
        graph.scale = scale

    return graph