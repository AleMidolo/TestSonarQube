from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged:
            existing_value_node = merged[key]
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Deep merge the MappingNodes
                existing_value = existing_value_node.value
                new_value = value_node.value
                
                # Create a dictionary to hold the merged key-value pairs
                merged_dict = {}
                for k, v in existing_value:
                    merged_dict[k.value] = v
                
                for k, v in new_value:
                    merged_dict[k.value] = v
                
                # Convert the merged dictionary back to a list of tuples
                merged_value = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_dict.items()]
                merged[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If either of the values is not a MappingNode, the last one wins
                merged[key] = value_node
        else:
            merged[key] = value_node
    
    # Convert the merged dictionary back to a list of tuples
    result = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]
    return result