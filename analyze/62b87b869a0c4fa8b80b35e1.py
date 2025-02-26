def hist_to_graph(hist, make_value=None, get_coordinate="left",
                  field_names=("x", "y"), scale=None):
    if make_value is None:
        make_value = lambda bin_: bin_.content

    coordinates = []
    for bin_ in hist.bins:
        if get_coordinate == "left":
            x = bin_.left
        elif get_coordinate == "right":
            x = bin_.right
        elif get_coordinate == "middle":
            x = bin_.center
        else:
            raise ValueError("Invalid value for get_coordinate. Choose 'left', 'right', or 'middle'.")

        value = make_value(bin_)
        if isinstance(value, tuple):
            coordinates.append((x, *value))
        else:
            coordinates.append((x, value))

    if scale is True:
        # Implement scaling logic if needed
        pass

    graph = create_graph(coordinates, field_names)
    return graph

def create_graph(coordinates, field_names):
    # Placeholder for graph creation logic
    return {"coordinates": coordinates, "field_names": field_names}