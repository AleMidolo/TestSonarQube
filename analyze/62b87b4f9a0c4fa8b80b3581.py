def scale(self, other=None, recompute=False):
    """
    计算或设置直方图的比例（积分值）。

    如果参数 *other* 为 ``None``，则返回当前直方图的比例。
    如果之前未计算过比例值，则会计算并存储该值以供后续使用（除非明确要求重新计算）。
    请注意，在对直方图进行更改（填充数据）后，如果之前已计算过比例值，则需要显式地重新计算比例。

    如果提供了一个浮点数 *other*，则将当前直方图的比例调整为 *other*。

    无法对比例为零的直方图进行重新调整。如果尝试这样做，将会引发 :exc:`.LenaValueError` 异常。
    """
    if other is None:
        if not hasattr(self, '_scale') or recompute:
            # 计算比例值
            self._scale = self._compute_scale()
        return self._scale
    else:
        if not isinstance(other, (int, float)):
            raise TypeError("Scale must be a float or integer.")
        if self._scale == 0:
            raise LenaValueError("Cannot rescale a histogram with zero scale.")
        # 调整比例
        self._scale = other
        return self._scale

def _compute_scale(self):
    """
    计算直方图的比例值（积分值）。
    """
    # 假设 self._data 是直方图的数据
    return sum(self._data)