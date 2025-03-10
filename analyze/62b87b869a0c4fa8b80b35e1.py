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
    from collections import namedtuple
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
    values = [make_value(bin_) for bin_ in hist.bins]

    # Ensure the number of field names matches the dimension of the values
    if len(field_names) != len(values[0]) + 1:
        raise ValueError("Number of field names must match the dimension of the result")

    # Create the graph
    Graph = namedtuple('Graph', field_names)
    graph_points = [Graph(x=coord, **dict(zip(field_names[1:], val))) for coord, val in zip(coordinates, values)]

    return graph_points