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

    if scale is None:
        scale = hist.scale if hasattr(hist, 'scale') else None

    x_coords = []
    y_values = []

    for bin_ in hist.bins:
        if get_coordinate == "left":
            x_coord = bin_.left_edge
        elif get_coordinate == "right":
            x_coord = bin_.right_edge
        elif get_coordinate == "middle":
            x_coord = (bin_.left_edge + bin_.right_edge) / 2
        else:
            raise ValueError("Invalid get_coordinate value. Must be 'left', 'right', or 'middle'.")

        y_value = make_value(bin_)

        x_coords.append(x_coord)
        y_values.append(y_value)

    x_coords = np.array(x_coords)
    y_values = np.array(y_values)

    if len(field_names) != y_values.shape[1] + 1:
        raise ValueError("Number of field_names must match the dimensionality of the result.")

    graph = {
        field_names[0]: x_coords,
        **{field_names[i + 1]: y_values[:, i] for i in range(y_values.shape[1])}
    }

    if scale is not None:
        graph['scale'] = scale

    return graph