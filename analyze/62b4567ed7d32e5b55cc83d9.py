from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Merge the MappingNodes deeply
                existing_value = existing_value_node.value
                new_value = value_node.value
                
                # Convert the list of tuples to a dictionary for easier merging
                existing_dict = {k.value: v for k, v in existing_value}
                new_dict = {k.value: v for k, v in new_value}
                
                # Merge the dictionaries
                for k, v in new_dict.items():
                    if k in existing_dict and isinstance(existing_dict[k], MappingNode) and isinstance(v, MappingNode):
                        # Recursively merge nested MappingNodes
                        merged_value = deep_merge_nodes([(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)])
                        existing_dict[k] = merged_value[0][1]
                    else:
                        # Overwrite or add the new value
                        existing_dict[k] = v
                
                # Convert the dictionary back to a list of tuples
                merged_value_list = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_dict.items()]
                merged_nodes[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value_list)
            else:
                # If either value is not a MappingNode, the new value prevails
                merged_nodes[key] = value_node
        else:
            # If the key is not in the merged_nodes, just add it
            merged_nodes[key] = value_node
    
    # Convert the merged_nodes dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]