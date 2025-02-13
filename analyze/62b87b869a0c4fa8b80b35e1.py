def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_

    coordinates = []
    values = []

    for i, bin_ in enumerate(hist):
        if get_coordinate == "left":
            coord = bin_.left
        elif get_coordinate == "right":
            coord = bin_.right
        elif get_coordinate == "middle":
            coord = bin_.center
        else:
            raise ValueError("get_coordinate must be 'left', 'right', or 'middle'")

        coordinates.append(coord)
        values.append(make_value(bin_))

    if scale is True:
        # Assuming hist has a scale method or attribute
        scale = hist.scale()

    graph_data = {field_names[i]: values[i] for i in range(len(field_names))}
    return graph_data