def difference(d1, d2, level=-1):
    """
    返回一个字典，其中包含 *d1* 中不在 *d2* 中的项。

    参数 *level* 用于设置递归的最大深度。对于无限递归，则将其设置为-1。如果设置为 1，当某个键同时存在于 *d1* 和 *d2* 中但其值不同，则该键值对会包含在差异结果中。
    有关更多详细信息，请参阅 :func:`intersection`。

    *d1* 和 *d2* 本身不会被修改。然而，*d1* 或其某些子字典可能会直接作为返回值。如果需要，请对结果进行深拷贝。

    .. 版本新增:: 0.5  
      添加了关键字参数 *level*。
    """
    def _difference(d1, d2, current_level):
        if current_level == 0:
            return {}
        
        diff = {}
        for key, value in d1.items():
            if key not in d2:
                diff[key] = value
            elif isinstance(value, dict) and isinstance(d2[key], dict):
                nested_diff = _difference(value, d2[key], current_level - 1 if current_level > 0 else -1)
                if nested_diff:
                    diff[key] = nested_diff
            elif value != d2[key]:
                diff[key] = value
        return diff

    return _difference(d1, d2, level)