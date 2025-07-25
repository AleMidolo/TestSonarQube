def deep_merge_nodes(nodes):
    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged:
            existing_value_node = merged[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # 深度合并 MappingNode
                existing_value = existing_value_node.value
                new_value = value_node.value
                
                # 将 new_value 合并到 existing_value 中
                existing_dict = {k.value: v for k, v in existing_value}
                new_dict = {k.value: v for k, v in new_value}
                
                # 合并字典
                for k, v in new_dict.items():
                    if k in existing_dict and isinstance(existing_dict[k], MappingNode) and isinstance(v, MappingNode):
                        # 递归合并嵌套的 MappingNode
                        existing_dict[k] = deep_merge_nodes([(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)])
                    else:
                        # 非 MappingNode 直接覆盖
                        existing_dict[k] = v
                
                # 转换回 MappingNode
                merged[key] = MappingNode(
                    tag='tag:yaml.org,2002:map',
                    value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_dict.items()]
                )
            else:
                # 非 MappingNode 直接覆盖
                merged[key] = value_node
        else:
            # 新键直接添加
            merged[key] = value_node
    
    # 转换回元组列表
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]