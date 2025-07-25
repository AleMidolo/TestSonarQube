def hist_to_graph(hist, make_value=None, get_coordinate="left", field_names=("x", "y"), scale=None):
    """
    将一个 :class:`.histogram` 转换为一个 :class:`.graph`。

    *make_value* 是一个函数，用于设置图形点的值。
    默认情况下，它是直方图的 bin 内容。
    *make_value* 接受一个单一值（bin 内容），不需要上下文。

    此选项可以用于创建图形的误差条。
    例如，要从一个包含名为 *mean*、*mean_error* 字段和上下文的 bin 的直方图中创建带误差的图形，可以使用以下代码：
    >>> make_value = lambda bin_: (bin_.mean, bin_.mean_error)

    *get_coordinate* 定义了从直方图 bin 创建的图表点的坐标位置，可选值包括 "left"（默认）、"right" 和 "middle"。

    *field_names* 设置图形的字段名称。字段名称的数量必须与结果的维度相同。对于上述的 *make_value*，字段名称可以是 *("x", "y_mean", "y_mean_error")*。

    *scale* 设置图形的比例（默认情况下未知）。
    如果设置为真，则使用直方图的比例。

    *hist* 必须仅包含数值型 bin（没有上下文），或者 *make_value* 在创建数值型图形时必须移除上下文。

    返回生成的图形。
    """
    import numpy as np

    if make_value is None:
        make_value = lambda bin_: bin_

    # Determine the coordinates based on the get_coordinate parameter
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

    # Ensure the number of field names matches the dimensionality of the values
    if len(field_names) != len(values[0]) + 1:
        raise ValueError("Number of field names must match the dimensionality of the values")

    # Create the graph
    graph = {
        field_names[0]: coordinates,
        **{field_names[i+1]: [v[i] for v in values] for i in range(len(values[0]))}
    }

    # Apply scale if provided
    if scale is not None:
        if scale:
            graph["scale"] = hist.scale
        else:
            graph["scale"] = None

    return graph