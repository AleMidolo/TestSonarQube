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
                
                # Convert the list of tuples to a dictionary for easier merging
                existing_dict = {k.value: v for k, v in existing_value}
                new_dict = {k.value: v for k, v in new_value}
                
                # Merge the dictionaries, with new values overwriting existing ones
                merged_dict = {**existing_dict, **new_dict}
                
                # Convert the merged dictionary back to a list of tuples
                merged_value = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_dict.items()]
                
                # Create a new MappingNode with the merged value
                merged[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If either node is not a MappingNode, the new value overwrites the existing one
                merged[key] = value_node
        else:
            # If the key is not in the merged dictionary, just add it
            merged[key] = value_node
    
    # Convert the merged dictionary back to a list of tuples
    result = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]
    
    return result