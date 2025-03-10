from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged:
            existing_value_node = merged[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Deep merge the MappingNodes
                existing_items = {k.value: v for k, v in existing_value_node.value}
                new_items = {k.value: v for k, v in value_node.value}
                
                # Merge the dictionaries, with new items overwriting existing ones
                merged_items = {**existing_items, **new_items}
                
                # Convert back to list of tuples
                merged_value = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_items.items()]
                merged[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If either is not a MappingNode, the new value overwrites the old one
                merged[key] = value_node
        else:
            merged[key] = value_node
    
    # Convert the merged dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]