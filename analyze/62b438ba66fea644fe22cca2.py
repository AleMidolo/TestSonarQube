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
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # 深度合并 MappingNode
                merged_value = deep_merge_nodes(existing_value_node.value + value_node.value)
                merged_nodes[key] = MappingNode(tag=existing_value_node.tag, value=merged_value)
            else:
                # 非 MappingNode 冲突，保留最后一个值
                merged_nodes[key] = value_node
        else:
            merged_nodes[key] = value_node
    
    # 将合并后的节点转换回元组列表形式
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=key), value_node) for key, value_node in merged_nodes.items()]