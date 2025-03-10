from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged:
            existing_value_node = merged[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Merge the MappingNodes
                existing_mapping = {k.value: v for k, v in existing_value_node.value}
                new_mapping = {k.value: v for k, v in value_node.value}
                
                # Deep merge the mappings
                for k, v in new_mapping.items():
                    if k in existing_mapping and isinstance(existing_mapping[k], MappingNode) and isinstance(v, MappingNode):
                        # Recursively merge nested MappingNodes
                        merged_nodes = deep_merge_nodes([(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)])
                        existing_mapping[k] = merged_nodes[0][1]
                    else:
                        # Overwrite or add new key-value pair
                        existing_mapping[k] = v
                
                # Convert back to list of tuples
                merged[key] = MappingNode(
                    tag='tag:yaml.org,2002:map',
                    value=[(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in existing_mapping.items()]
                )
            else:
                # If either value is not a MappingNode, the last value prevails
                merged[key] = value_node
        else:
            # If the key is not in the merged dict, just add it
            merged[key] = value_node
    
    # Convert the merged dict back to a list of tuples
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v) for k, v in merged.items()]