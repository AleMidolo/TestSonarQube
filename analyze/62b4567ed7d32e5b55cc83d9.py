from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Merge the MappingNodes deeply
                existing_items = {item[0].value: item[1] for item in existing_value_node.value}
                new_items = {item[0].value: item[1] for item in value_node.value}
                
                # Update existing_items with new_items, merging deeply if necessary
                for new_key, new_value in new_items.items():
                    if new_key in existing_items and isinstance(existing_items[new_key], MappingNode) and isinstance(new_value, MappingNode):
                        # Recursively merge nested MappingNodes
                        merged_nested_nodes = deep_merge_nodes([(ScalarNode(tag='tag:yaml.org,2002:str', value=new_key), new_value])
                        existing_items[new_key] = merged_nested_nodes[0][1]
                    else:
                        # Overwrite or add new key-value pair
                        existing_items[new_key] = new_value
                
                # Convert the merged dictionary back to a list of tuples
                merged_value = [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_items.items()]
                merged_nodes[key] = MappingNode(tag='tag:yaml.org,2002:map', value=merged_value)
            else:
                # If either value is not a MappingNode, the last value prevails
                merged_nodes[key] = value_node
        else:
            # If the key is not in the merged_nodes, add it
            merged_nodes[key] = value_node
    
    # Convert the merged_nodes dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged_nodes.items()]