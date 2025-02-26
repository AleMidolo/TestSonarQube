def scale(self, other=None):
    """
    获取或设置图表的比例。

    如果参数 *other* 为 ``None``，则返回此图表的比例。

    如果提供了一个数值类型的 *other*，则将图表重新缩放到该值。
    如果图表的比例未知或为零，对其重新缩放将会引发:exc: `~.LenaValueError` 异常。

    为了获得有意义的结果，将使用图表的字段。
    仅最后一个坐标会被重新缩放。
    例如，如果图表具有 *x* 和 *y* 坐标，则 *y* 会被重新缩放；对于三维图表，*z* 会被重新缩放。
    所有的误差值也会与其对应的坐标一起重新缩放。
    """
    if other is None:
        return self.scale_value  # 假设 self.scale_value 存储当前比例

    if not isinstance(other, (int, float)):
        raise TypeError("参数 *other* 必须是数值类型")

    if self.scale_value is None or self.scale_value == 0:
        raise LenaValueError("图表的比例未知或为零，无法重新缩放")

    # 假设 self.data 存储图表的数据，self.errors 存储误差值
    last_coordinate_index = -1  # 假设最后一个坐标的索引
    scale_factor = other / self.scale_value

    # 重新缩放数据和误差值
    self.data[last_coordinate_index] *= scale_factor
    self.errors[last_coordinate_index] *= scale_factor

    # 更新比例
    self.scale_value = other