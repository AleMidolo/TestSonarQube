from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Merge the values of the MappingNodes
                existing_value = existing_value_node.value
                new_value = value_node.value
                
                # Create a dictionary to hold the merged key-value pairs
                merged_value = {}
                for k_node, v_node in existing_value:
                    merged_value[k_node.value] = v_node
                
                for k_node, v_node in new_value:
                    merged_value[k_node.value] = v_node
                
                # Convert the merged dictionary back to a list of tuples
                merged_value_list = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_value.items()]
                
                # Update the existing MappingNode with the merged values
                merged_nodes[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value_list)
            else:
                # If either node is not a MappingNode, prefer the new value
                merged_nodes[key] = value_node
        else:
            # If the key is not already in the merged_nodes, add it
            merged_nodes[key] = value_node
    
    # Convert the merged_nodes dictionary back to a list of tuples
    result = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]
    
    return result