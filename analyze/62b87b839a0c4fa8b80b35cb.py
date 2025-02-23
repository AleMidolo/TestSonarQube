def _get_err_indices(self, coord_name):
    """
    查找与 `coord_name` 对应的所有错误索引。
    获取与某个坐标对应的错误索引。
    """
    err_indices = []
    for index, coord in enumerate(self.coordinates):
        if coord == coord_name and self.errors[index]:
            err_indices.append(index)
    return err_indices