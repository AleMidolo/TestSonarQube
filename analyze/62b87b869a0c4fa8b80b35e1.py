def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    """
    Convert a :class:`.histogram` to a :class:`.graph`.

    *make_value* is a function to set the value of a graph's point.
    By default it is bin content.
    *make_value* accepts a single value (bin content) without context.

    This option could be used to create graph's error bars.
    For example, to create a graph with errors
    from a histogram where bins contain
    a named tuple with fields *mean*, *mean_error* and a context
    one could use

    >>> make_value = lambda bin_: (bin_.mean, bin_.mean_error)

    *get_coordinate* defines what the coordinate
    of a graph point created from a histogram bin will be.
    It can be "left" (default), "right" and "middle".

    *field_names* set field names of the graph. Their number
    must be the same as the dimension of the result.
    For a *make_value* above they would be
    *("x", "y_mean", "y_mean_error")*.

    *scale* becomes the graph's scale (unknown by default).
    If it is ``True``, it uses the histogram scale.

    *hist* must contain only numeric bins (without context)
    or *make_value* must remove context when creating a numeric graph.

    Return the resulting graph.
    """
    import numpy as np

    if make_value is None:
        make_value = lambda bin_: bin_

    if scale is True:
        scale = hist.scale

    # Determine the coordinate for each bin
    if get_coordinate == "left":
        coordinates = hist.bin_edges[:-1]
    elif get_coordinate == "right":
        coordinates = hist.bin_edges[1:]
    elif get_coordinate == "middle":
        coordinates = (hist.bin_edges[:-1] + hist.bin_edges[1:]) / 2
    else:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    # Apply make_value to each bin
    values = [make_value(bin_) for bin_ in hist.bin_contents]

    # Ensure values are in a consistent format (e.g., tuples for error bars)
    if isinstance(values[0], (tuple, list)):
        values = np.array(values)
    else:
        values = np.array([(v,) for v in values])

    # Combine coordinates and values into a structured array
    dtype = [(field_names[0], float)] + [(field_names[i], float) for i in range(1, values.shape[1] + 1)]
    graph_data = np.empty(len(coordinates), dtype=dtype)
    graph_data[field_names[0]] = coordinates
    for i in range(1, values.shape[1] + 1):
        graph_data[field_names[i]] = values[:, i - 1]

    # Create the graph
    from graph import Graph
    graph = Graph(graph_data, scale=scale)

    return graph