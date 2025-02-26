def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_

    coordinates = []
    for bin_ in hist:
        if get_coordinate == "left":
            x = bin_.left
        elif get_coordinate == "right":
            x = bin_.right
        elif get_coordinate == "middle":
            x = bin_.center
        else:
            raise ValueError("get_coordinate must be 'left', 'right', or 'middle'.")

        value = make_value(bin_)
        if isinstance(value, tuple):
            coordinates.append((x, *value))
        else:
            coordinates.append((x, value))

    if scale is True:
        # Implement scaling logic if needed
        pass

    graph = {field_names[i]: [coord[i] for coord in coordinates] for i in range(len(field_names))}
    return graph