from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged:
            existing_value_node = merged[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Deep merge the MappingNodes
                existing_mapping = dict(existing_value_node.value)
                new_mapping = dict(value_node.value)
                
                for new_key_node, new_value_node in new_mapping.items():
                    new_key = new_key_node.value
                    
                    if new_key in existing_mapping:
                        existing_value = existing_mapping[new_key]
                        
                        if isinstance(existing_value, MappingNode) and isinstance(new_value_node, MappingNode):
                            # Recursively deep merge nested MappingNodes
                            merged_value = deep_merge_nodes([(new_key_node, existing_value), (new_key_node, new_value_node)])
                            existing_mapping[new_key_node] = merged_value[0][1]
                        else:
                            # Overwrite with the new value
                            existing_mapping[new_key_node] = new_value_node
                    else:
                        # Add the new key-value pair
                        existing_mapping[new_key_node] = new_value_node
                
                merged[key] = MappingNode(existing_value_node.tag, list(existing_mapping.items()))
            else:
                # Overwrite with the new value if either is not a MappingNode
                merged[key] = value_node
        else:
            # Add the new key-value pair
            merged[key] = value_node
    
    return [(ScalarNode(key_node.tag, key), value_node) for key, value_node in merged.items()]