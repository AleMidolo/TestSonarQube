def _get_err_indices(self, coord_name):
    """
    查找与 `coord_name` 对应的所有错误索引。
    获取与某个坐标对应的错误索引。
    """
    # 假设有一个字典存储坐标名和对应的错误索引
    error_indices = {
        'coord1': [1, 2, 3],
        'coord2': [4, 5],
        'coord3': [6, 7, 8, 9]
    }
    
    # 返回与 coord_name 对应的错误索引，如果不存在则返回空列表
    return error_indices.get(coord_name, [])