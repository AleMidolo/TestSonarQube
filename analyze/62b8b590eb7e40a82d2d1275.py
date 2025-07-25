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
    seen = set()
    
    # 遍历所有排序列表
    for ordering in orderings:
        # 遍历当前列表中的每个元素
        for element in ordering:
            # 如果元素已经在结果中,跳过
            if element in seen:
                continue
                
            # 检查是否可以添加当前元素
            can_add = True
            # 获取当前元素在所有列表中的位置
            positions = element_positions[element]
            
            # 检查当前元素前面的所有元素是否都已经处理过
            for ordering_idx, pos in enumerate(positions):
                # 检查当前位置之前的元素
                for prev_pos in range(pos):
                    prev_element = orderings[ordering_idx][prev_pos]
                    if prev_element not in seen:
                        can_add = False
                        break
                if not can_add:
                    break
                    
            # 如果可以添加当前元素
            if can_add:
                result.append(element)
                seen.add(element)
                
    return result