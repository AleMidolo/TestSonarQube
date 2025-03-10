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
        # Find the next element to add
        next_element = None
        for ordering in orderings:
            for element in ordering:
                if element not in seen:
                    next_element = element
                    break
            if next_element is not None:
                break
        
        if next_element is None:
            break
        
        # Add the next element to the merged list
        merged.append(next_element)
        seen.add(next_element)
        
        # Remove the element from all orderings
        for ordering in orderings:
            if next_element in ordering:
                ordering.remove(next_element)
    
    return merged