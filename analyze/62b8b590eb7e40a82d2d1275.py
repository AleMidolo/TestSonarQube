def _legacy_mergeOrderings(orderings):
    """
    将多个列表按出现顺序合并为一个不包含重复元素的列表。
    合并多个排序列表（orderings），同时保留每个排序列表中的顺序。

    这些排序列表受到以下约束：如果某个对象出现在两个或多个排序列表中，那么以该对象为起点的后缀部分必须在所有相关的排序列表中一致。

    例如：
    >>> _mergeOrderings([
    ... ['x', 'y', 'z'],
    ... ['q', 'z'],
    ... [1, 3, 5],
    ... ['z']
    ... ])
    ['x', 'y', 'q', 1, 3, 5, 'z']
    """
    merged = []
    for ordering in orderings:
        for item in ordering:
            if item not in merged:
                merged.append(item)
    return merged