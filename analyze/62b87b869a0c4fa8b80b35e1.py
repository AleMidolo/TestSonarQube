def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_

    if get_coordinate not in ["left", "right", "middle"]:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    graph_data = []
    bin_width = hist.bin_width
    for i, bin_ in enumerate(hist.bins):
        value = make_value(bin_)
        if get_coordinate == "left":
            x = hist.bin_edges[i]
        elif get_coordinate == "right":
            x = hist.bin_edges[i + 1]
        else:  # get_coordinate == "middle"
            x = (hist.bin_edges[i] + hist.bin_edges[i + 1]) / 2

        graph_data.append((x,) + value)

    if scale is True:
        # Apply histogram scale to graph data if needed
        pass  # Implement scaling logic if necessary

    return Graph(data=graph_data, field_names=field_names)