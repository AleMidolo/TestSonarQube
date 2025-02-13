def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_

    if get_coordinate not in ["left", "right", "middle"]:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    graph_data = []
    bin_edges = hist.edges
    bin_contents = hist.contents

    for i, content in enumerate(bin_contents):
        if get_coordinate == "left":
            x = bin_edges[i]
        elif get_coordinate == "right":
            x = bin_edges[i + 1]
        else:  # middle
            x = (bin_edges[i] + bin_edges[i + 1]) / 2

        value = make_value(content)
        if isinstance(value, tuple):
            graph_data.append((x, *value))
        else:
            graph_data.append((x, value))

    if scale is True:
        graph_scale = hist.scale
    else:
        graph_scale = scale

    return Graph(data=graph_data, field_names=field_names, scale=graph_scale)