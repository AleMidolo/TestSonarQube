from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Merge the MappingNodes deeply
                existing_mapping = dict(existing_value_node.value)
                new_mapping = dict(value_node.value)
                
                for sub_key_node, sub_value_node in new_mapping.items():
                    sub_key = sub_key_node.value
                    if sub_key in existing_mapping:
                        existing_sub_value_node = existing_mapping[sub_key]
                        if isinstance(existing_sub_value_node, MappingNode) and isinstance(sub_value_node, MappingNode):
                            # Recursively merge nested MappingNodes
                            merged_sub_value_node = deep_merge_nodes([(sub_key_node, existing_sub_value_node), (sub_key_node, sub_value_node)])
                            existing_mapping[sub_key_node] = merged_sub_value_node[0][1]
                        else:
                            # Overwrite non-MappingNode values
                            existing_mapping[sub_key_node] = sub_value_node
                    else:
                        existing_mapping[sub_key_node] = sub_value_node
                
                merged_nodes[key] = MappingNode(existing_value_node.tag, list(existing_mapping.items()))
            else:
                # Overwrite non-MappingNode values
                merged_nodes[key] = value_node
        else:
            merged_nodes[key] = value_node
    
    return [(ScalarNode(key_node.tag, key), value_node) for key, value_node in merged_nodes.items()]