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
        return self._scale
    elif isinstance(other, (int, float)):
        if self._scale == 0 or self._scale is None:
            raise ValueError("Cannot rescale chart with unknown or zero scale.")
        scaling_factor = other / self._scale
        # Rescale the last coordinate
        if hasattr(self, 'y'):
            self.y *= scaling_factor
            if hasattr(self, 'y_err'):
                self.y_err *= scaling_factor
        elif hasattr(self, 'z'):
            self.z *= scaling_factor
            if hasattr(self, 'z_err'):
                self.z_err *= scaling_factor
        self._scale = other
    else:
        raise TypeError("Scale must be a numeric value or None.")