def _legacy_mergeOrderings(orderings):
    # 创建一个字典来存储每个元素在各个列表中的位置
    element_positions = {}
    
    # 遍历所有排序列表
    for ordering in orderings:
        for pos, element in enumerate(ordering):
            if element not in element_positions:
                element_positions[element] = []
            element_positions[element].append(pos)
            
    # 创建结果列表
    result = []
    # 记录已处理的元素
    used = set()
    
    # 持续处理直到所有元素都被使用
    while len(used) < len(element_positions):
        # 找到当前可以添加的元素
        # 元素必须在其所在的所有列表中,其之前的元素都已经被使用
        next_element = None
        
        for element, positions in element_positions.items():
            if element in used:
                continue
                
            can_use = True
            # 检查该元素在每个包含它的列表中,是否其前面的元素都已使用
            for ordering in orderings:
                if element in ordering:
                    idx = ordering.index(element)
                    # 检查该元素之前的元素是否都已使用
                    for i in range(idx):
                        if ordering[i] not in used:
                            can_use = False
                            break
                    if not can_use:
                        break
                        
            if can_use:
                next_element = element
                break
                
        if next_element is None:
            raise ValueError("Cannot merge orderings - circular dependency detected")
            
        result.append(next_element)
        used.add(next_element)
        
    return result