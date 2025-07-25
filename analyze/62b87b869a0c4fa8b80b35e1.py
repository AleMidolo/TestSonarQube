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

    # Determine the coordinate for each bin
    if get_coordinate == "left":
        coordinates = hist.bin_edges[:-1]
    elif get_coordinate == "right":
        coordinates = hist.bin_edges[1:]
    elif get_coordinate == "middle":
        coordinates = (hist.bin_edges[:-1] + hist.bin_edges[1:]) / 2
    else:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    # Default make_value function if not provided
    if make_value is None:
        make_value = lambda bin_content: bin_content

    # Extract values from histogram bins
    values = [make_value(bin_content) for bin_content in hist.bin_contents]

    # Determine the number of fields required
    if isinstance(values[0], (tuple, list)):
        num_fields = len(values[0]) + 1  # +1 for the x-coordinate
    else:
        num_fields = 2  # x and y

    # Ensure field_names has the correct length
    if len(field_names) != num_fields:
        raise ValueError(f"field_names must have {num_fields} elements")

    # Create the graph data structure
    GraphPoint = namedtuple('GraphPoint', field_names)
    graph_data = []

    for coord, value in zip(coordinates, values):
        if isinstance(value, (tuple, list)):
            graph_data.append(GraphPoint(coord, *value))
        else:
            graph_data.append(GraphPoint(coord, value))

    # Determine the scale
    if scale is True:
        scale = hist.scale
    elif scale is None:
        scale = "unknown"

    # Create and return the graph
    Graph = namedtuple('Graph', ['data', 'scale'])
    return Graph(data=graph_data, scale=scale)