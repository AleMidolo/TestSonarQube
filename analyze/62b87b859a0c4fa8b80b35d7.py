def to_csv(self, separator=", ", header=None):
    """
    .. 已废弃:: 0.5 在 Lena 0.5 中，`to_csv` 不再使用。
        可迭代对象将被转换为表格。

    将图的点转换为 CSV 格式。

    *separator* 用于分隔值，默认是逗号。

    *header* 如果不为 ``None``，将作为输出的第一行字符串
    （会自动添加换行符）。

    由于图可以是多维的，
    对于每个点，首先将其坐标转换为字符串
    （用 *separator* 分隔），然后再处理其值的每个部分。

    要在 Lena 序列中将 :class:`Graph` 转换为 CSV，
    请使用 :class:`lena.output.ToCSV`。
    """
    # Assuming self.points is a list of points in the graph
    csv_lines = []
    
    if header is not None:
        csv_lines.append(header + "\n")
    
    for point in self.points:
        # Convert point coordinates to string and join with separator
        point_str = separator.join(map(str, point.coordinates))
        # Convert point values to string and join with separator
        values_str = separator.join(map(str, point.values))
        # Combine point string and values string
        csv_lines.append(f"{point_str}{separator}{values_str}\n")
    
    return ''.join(csv_lines)