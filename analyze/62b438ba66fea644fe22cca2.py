def deep_merge_nodes(nodes):
    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged:
            existing_value_node = merged[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Recursively merge the MappingNodes
                merged_value = deep_merge_nodes(existing_value_node.value + value_node.value)
                merged[key] = MappingNode(tag=existing_value_node.tag, value=merged_value)
            else:
                # If either value is not a MappingNode, keep the last value
                merged[key] = value_node
        else:
            merged[key] = value_node
    
    # Convert the merged dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=key), value_node) for key, value_node in merged.items()]