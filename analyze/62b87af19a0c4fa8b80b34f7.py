def difference(d1, d2, level=-1):
    """
    返回一个字典，其中包含 *d1* 中不在 *d2* 中的项。

    参数 *level* 用于设置递归的最大深度。对于无限递归，则将其设置为-1。如果设置为 1，当某个键同时存在于 *d1* 和 *d2* 中但其值不同，则该键值对会包含在差异结果中。
    有关更多详细信息，请参阅 :func:`intersection`。

    *d1* 和 *d2* 本身不会被修改。然而，*d1* 或其某些子字典可能会直接作为返回值。如果需要，请对结果进行深拷贝。
    """
    result = {}
    
    # 遍历d1中的所有键值对
    for key, value in d1.items():
        # 如果键不在d2中，直接添加到结果中
        if key not in d2:
            result[key] = value
        # 如果键在d2中且level不为0
        elif level != 0:
            # 如果两个值都是字典，则递归比较
            if isinstance(value, dict) and isinstance(d2[key], dict):
                # 递归调用，level减1
                nested_diff = difference(value, d2[key], level-1 if level > 0 else -1)
                if nested_diff:
                    result[key] = nested_diff
            # 如果值不相等，且level为1或-1，则添加到结果中
            elif value != d2[key]:
                result[key] = value
                
    return result