def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Deep merge the MappingNodes
                existing_value = existing_value_node.value
                new_value = value_node.value
                
                # Create a dictionary to hold the merged values
                merged_value = {}
                
                # Add all existing values
                for existing_key_node, existing_sub_value_node in existing_value:
                    merged_value[existing_key_node.value] = existing_sub_value_node
                
                # Add or overwrite with new values
                for new_key_node, new_sub_value_node in new_value:
                    merged_value[new_key_node.value] = new_sub_value_node
                
                # Convert the merged dictionary back to a list of tuples
                merged_value_list = [
                    (ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)
                    for k, v in merged_value.items()
                ]
                
                # Update the merged_nodes with the new merged MappingNode
                merged_nodes[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value_list)
            else:
                # If either value is not a MappingNode, keep the last value
                merged_nodes[key] = value_node
        else:
            # If the key is not in merged_nodes, just add it
            merged_nodes[key] = value_node
    
    # Convert the merged_nodes dictionary back to a list of tuples
    result = [
        (ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)
        for k, v in merged_nodes.items()
    ]
    
    return result