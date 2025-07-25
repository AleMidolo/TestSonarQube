from ruamel.yaml.nodes import ScalarNode, MappingNode

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
                
                # Create a dictionary to hold the merged key-value pairs
                merged_dict = {}
                for k_node, v_node in existing_value:
                    merged_dict[k_node.value] = v_node
                
                for k_node, v_node in new_value:
                    merged_dict[k_node.value] = v_node
                
                # Convert the merged dictionary back to a list of tuples
                merged_value = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_dict.items()]
                merged_nodes[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If either value is not a MappingNode, the last value wins
                merged_nodes[key] = value_node
        else:
            # If the key is not in the merged_nodes, just add it
            merged_nodes[key] = value_node
    
    # Convert the merged_nodes dictionary back to a list of tuples
    result = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]
    return result