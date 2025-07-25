def deep_merge_nodes(nodes):
    """
    合并任何与重复键对应的节点值并返回结果。如果存在具有非 `MappingNode` 值的冲突键，则保留最后一个值。

    给定一个嵌套的 borgmatic 配置数据结构，其形式为一个元组列表：
    (
        ruamel.yaml.nodes.ScalarNode as a key,
        ruamel.yaml.nodes.MappingNode or other Node as a value,
    ),

    对任何与重复键对应的节点值进行深度合并，并返回合并后的结果。如果存在具有非 `MappingNode` 值（例如整数或字符串）的冲突键，则以最后一个值为准。
    """
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, type(value_node)) and isinstance(existing_value_node, type(value_node)):
                if isinstance(existing_value_node, type(value_node)) and isinstance(existing_value_node, type(value_node)):
                    # Both are MappingNodes, perform deep merge
                    existing_mapping = existing_value_node.value
                    new_mapping = value_node.value
                    
                    # Create a dictionary to hold the merged mapping
                    merged_mapping = {}
                    
                    # Add all existing mappings
                    for existing_key_node, existing_value in existing_mapping:
                        merged_mapping[existing_key_node.value] = existing_value
                    
                    # Add or overwrite with new mappings
                    for new_key_node, new_value in new_mapping:
                        merged_mapping[new_key_node.value] = new_value
                    
                    # Convert the merged mapping back to a list of tuples
                    merged_mapping_list = [
                        (ScalarNode(tag='tag:yaml.org,2002:str', value=key), value
                        for key, value in merged_mapping.items()
                    ]
                    
                    # Create a new MappingNode with the merged mapping
                    merged_nodes[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_mapping_list)
                else:
                    # One of them is not a MappingNode, keep the last value
                    merged_nodes[key] = value_node
            else:
                # One of them is not a MappingNode, keep the last value
                merged_nodes[key] = value_node
        else:
            # Key not seen before, just add it
            merged_nodes[key] = value_node
    
    # Convert the merged_nodes dictionary back to a list of tuples
    result = [
        (ScalarNode(tag='tag:yaml.org,2002:str', value=key), value)
        for key, value in merged_nodes.items()
    ]
    
    return result