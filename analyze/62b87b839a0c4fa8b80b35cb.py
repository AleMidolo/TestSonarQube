def _get_err_indices(self, coord_name):
    """
    查找与 `coord_name` 对应的所有错误索引。
    获取与某个坐标对应的错误索引。
    """
    err_indices = []
    for i, coord in enumerate(self.coords):
        if coord == coord_name and self.errors[i]:
            err_indices.append(i)
    return err_indices