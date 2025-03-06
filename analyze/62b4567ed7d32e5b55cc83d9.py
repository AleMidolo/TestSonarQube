def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, ruamel.yaml.nodes.MappingNode) and isinstance(value_node, ruamel.yaml.nodes.MappingNode):
                # Deep merge the MappingNodes
                existing_value = existing_value_node.value
                new_value = value_node.value
                
                # Create a dictionary to hold the merged key-value pairs
                merged_dict = {}
                
                # Add all existing key-value pairs
                for existing_key_node, existing_val_node in existing_value:
                    merged_dict[existing_key_node.value] = existing_val_node
                
                # Add or overwrite with new key-value pairs
                for new_key_node, new_val_node in new_value:
                    merged_dict[new_key_node.value] = new_val_node
                
                # Convert the merged dictionary back to a list of tuples
                merged_value = [(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v] for k, v in merged_dict.items()]
                
                # Create a new MappingNode with the merged value
                merged_nodes[key] = ruamel.yaml.nodes.MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If either value is not a MappingNode, the last value wins
                merged_nodes[key] = value_node
        else:
            # If the key is not in the merged_nodes, just add it
            merged_nodes[key] = value_node
    
    # Convert the merged_nodes dictionary back to a list of tuples
    return [(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v] for k, v in merged_nodes.items()]