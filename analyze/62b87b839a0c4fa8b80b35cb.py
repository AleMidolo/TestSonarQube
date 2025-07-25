def _get_err_indices(self, coord_name):
    """
    查找与 `coord_name` 对应的所有错误索引。
    获取与某个坐标对应的错误索引。
    """
    # 假设 self.errors 是一个字典，键是坐标名称，值是错误索引的列表
    return self.errors.get(coord_name, [])