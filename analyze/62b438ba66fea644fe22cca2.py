def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, ruamel.yaml.nodes.MappingNode) and isinstance(value_node, ruamel.yaml.nodes.MappingNode):
                # Merge the MappingNodes
                existing_value = existing_value_node.value
                new_value = value_node.value
                
                # Convert the list of tuples to a dictionary for easier merging
                existing_dict = {k.value: v for k, v in existing_value}
                new_dict = {k.value: v for k, v in new_value}
                
                # Merge the dictionaries
                merged_dict = {**existing_dict, **new_dict}
                
                # Convert back to a list of tuples
                merged_value = [(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_dict.items()]
                
                # Create a new MappingNode with the merged value
                merged_nodes[key] = ruamel.yaml.nodes.MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If either value is not a MappingNode, the last value prevails
                merged_nodes[key] = value_node
        else:
            merged_nodes[key] = value_node
    
    # Convert the merged dictionary back to a list of tuples
    return [(ruamel.yaml.nodes.ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]