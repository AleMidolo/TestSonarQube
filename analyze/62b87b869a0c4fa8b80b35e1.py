def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_

    if get_coordinate not in ["left", "right", "middle"]:
        raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

    graph_data = []
    bin_width = hist.bin_width
    for i, bin_ in enumerate(hist.bins):
        if get_coordinate == "left":
            x = bin_.left
        elif get_coordinate == "right":
            x = bin_.right
        else:  # get_coordinate == "middle"
            x = bin_.center

        y_values = make_value(bin_)
        if isinstance(y_values, tuple):
            graph_data.append((x, *y_values))
        else:
            graph_data.append((x, y_values))

    if scale is True:
        # Apply histogram scale to the graph if needed
        pass  # Implement scaling logic if required

    return Graph(data=graph_data, field_names=field_names)