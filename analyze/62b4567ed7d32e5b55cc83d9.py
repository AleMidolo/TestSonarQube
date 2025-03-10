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
                for k, v in existing_value:
                    merged_dict[k.value] = v
                
                for k, v in new_value:
                    if k.value in merged_dict and isinstance(merged_dict[k.value], MappingNode) and isinstance(v, MappingNode):
                        # Recursively merge nested MappingNodes
                        merged_dict[k.value] = deep_merge_nodes([(k, merged_dict[k.value]), (k, v)])[0][1]
                    else:
                        # Overwrite or add the new value
                        merged_dict[k.value] = v
                
                # Convert the merged dictionary back to a list of tuples
                merged_value = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v] for k, v in merged_dict.items()]
                merged_nodes[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If either value is not a MappingNode, the last value prevails
                merged_nodes[key] = value_node
        else:
            # If the key is not in the merged_nodes, just add it
            merged_nodes[key] = value_node
    
    # Convert the merged_nodes dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]