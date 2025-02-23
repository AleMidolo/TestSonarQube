def difference(d1, d2, level=-1):
    """
    返回一个字典，其中包含 *d1* 中不在 *d2* 中的项。

    参数 *level* 用于设置递归的最大深度。对于无限递归，则将其设置为-1。如果设置为 1，当某个键同时存在于 *d1* 和 *d2* 中但其值不同，则该键值对会包含在差异结果中。
    有关更多详细信息，请参阅 :func:`intersection`。

    *d1* 和 *d2* 本身不会被修改。然而，*d1* 或其某些子字典可能会直接作为返回值。如果需要，请对结果进行深拷贝。

    .. 版本新增:: 0.5  
     添加了关键字参数 *level*。
    """
    if level == 0:
        return {}
    
    result = {}
    
    for key in d1:
        if key not in d2:
            result[key] = d1[key]
        else:
            if isinstance(d1[key], dict) and isinstance(d2[key], dict):
                if level != 1:
                    nested_diff = difference(d1[key], d2[key], level - 1)
                    if nested_diff:
                        result[key] = nested_diff
            elif d1[key] != d2[key]:
                result[key] = d1[key]
    
    return result