def deep_merge_nodes(nodes):
    from ruamel.yaml.nodes import MappingNode, ScalarNode

    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged:
            existing_value_node = merged[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Deep merge the MappingNodes
                existing_mapping = {k.value: v for k, v in existing_value_node.value}
                new_mapping = {k.value: v for k, v in value_node.value}
                
                # Merge the mappings
                for new_key, new_value in new_mapping.items():
                    if new_key in existing_mapping and isinstance(existing_mapping[new_key], MappingNode) and isinstance(new_value, MappingNode):
                        # Recursively merge nested MappingNodes
                        existing_mapping[new_key] = deep_merge_nodes([
                            (ScalarNode(tag='tag:yaml.org,2002:str', value=new_key), existing_mapping[new_key]),
                            (ScalarNode(tag='tag:yaml.org,2002:str', value=new_key), new_value)
                        ])[0][1]
                    else:
                        # Overwrite or add new key-value pair
                        existing_mapping[new_key] = new_value
                
                # Convert back to list of tuples
                merged[key] = MappingNode(
                    tag='tag:yaml.org,2002:map',
                    value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_mapping.items()]
                )
            else:
                # If either value is not a MappingNode, the new value takes precedence
                merged[key] = value_node
        else:
            # If the key is not in the merged dict, just add it
            merged[key] = value_node
    
    # Convert the merged dictionary back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]