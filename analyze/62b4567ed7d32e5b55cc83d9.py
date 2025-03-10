from ruamel.yaml.nodes import ScalarNode, MappingNode

def deep_merge_nodes(nodes):
    merged_nodes = {}
    
    for key_node, value_node in nodes:
        key = key_node.value
        
        if key in merged_nodes:
            existing_value_node = merged_nodes[key]
            
            if isinstance(existing_value_node, MappingNode) and isinstance(value_node, MappingNode):
                # Merge the MappingNodes
                existing_mapping = dict(existing_value_node.value)
                new_mapping = dict(value_node.value)
                
                for new_key_node, new_value_node in new_mapping.items():
                    existing_mapping[new_key_node] = new_value_node
                
                merged_nodes[key] = MappingNode(
                    tag=existing_value_node.tag,
                    value=list(existing_mapping.items()),
                )
            else:
                # If not both MappingNodes, overwrite with the new value
                merged_nodes[key] = value_node
        else:
            merged_nodes[key] = value_node
    
    return [(ScalarNode(tag='tag:yaml.org,2002:str', value=key), value_node) for key, value_node in merged_nodes.items()]