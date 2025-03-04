def _legacy_mergeOrderings(orderings):
    # 创建一个字典来存储每个元素在各个列表中的位置
    element_positions = {}
    
    # 遍历所有排序列表,记录每个元素出现的位置
    for ordering in orderings:
        for i, element in enumerate(ordering):
            if element not in element_positions:
                element_positions[element] = []
            element_positions[element].append(i)
            
    # 创建结果列表
    result = []
    # 记录已处理的元素
    seen = set()
    
    # 遍历所有排序列表
    for ordering in orderings:
        # 遍历当前列表中的每个元素
        for element in ordering:
            # 如果元素已经处理过则跳过
            if element in seen:
                continue
                
            # 检查该元素后面的所有元素是否在其他列表中保持一致的顺序
            valid = True
            for other_ordering in orderings:
                if element in other_ordering:
                    idx = other_ordering.index(element)
                    # 检查后缀是否一致
                    if idx < len(other_ordering) - 1:
                        suffix = other_ordering[idx + 1:]
                        for suffix_element in suffix:
                            if suffix_element in ordering[ordering.index(element) + 1:]:
                                if ordering[ordering.index(element) + 1:].index(suffix_element) != suffix.index(suffix_element):
                                    valid = False
                                    break
                    if not valid:
                        break
                        
            # 如果元素满足约束条件,则添加到结果列表中
            if valid:
                result.append(element)
                seen.add(element)
                
    return result