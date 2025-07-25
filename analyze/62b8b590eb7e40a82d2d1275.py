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
    seen = set()
    
    while True:
        # 找到所有列表的第一个元素
        candidates = []
        for ordering in orderings:
            if ordering:
                candidates.append(ordering[0])
        
        if not candidates:
            break
        
        # 找到所有候选元素中最先出现的元素
        for candidate in candidates:
            if candidate not in seen:
                merged.append(candidate)
                seen.add(candidate)
                # 从所有列表中移除该元素
                for ordering in orderings:
                    if ordering and ordering[0] == candidate:
                        ordering.pop(0)
                break
        else:
            # 如果没有找到新的元素，说明所有元素都已处理
            break
    
    return merged