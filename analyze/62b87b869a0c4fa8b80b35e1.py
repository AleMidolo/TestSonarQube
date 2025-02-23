def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_

    if get_coordinate not in ["left", "right", "middle"]:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    graph_data = []
    bin_width = hist.bin_edges[1] - hist.bin_edges[0]

    for i, bin_content in enumerate(hist.bins):
        if get_coordinate == "left":
            x = hist.bin_edges[i]
        elif get_coordinate == "right":
            x = hist.bin_edges[i + 1]
        else:  # get_coordinate == "middle"
            x = (hist.bin_edges[i] + hist.bin_edges[i + 1]) / 2

        y_values = make_value(bin_content)
        if isinstance(y_values, tuple):
            graph_data.append((x, *y_values))
        else:
            graph_data.append((x, y_values))

    if scale is True:
        # Apply histogram scale to graph data if needed
        pass  # Implement scaling logic if required

    return graph_data