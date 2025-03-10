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
                for new_key, new_value in new_mapping.items():
                    if new_key in existing_mapping and isinstance(existing_mapping[new_key], MappingNode) and isinstance(new_value, MappingNode):
                        # Recursively merge nested MappingNodes
                        merged[key] = MappingNode(
                            tag=existing_value_node.tag,
                            value=[
                                (ScalarNode(tag='tag:yaml.org,2002:str', value=k), 
                                deep_merge_nodes([(ScalarNode(tag='tag:yaml.org,2002:str', value=k), v)])[0][1] 
                                if k == new_key and isinstance(v, MappingNode) else v
                                for k, v in existing_value_node.value
                            ] + [
                                (k, v) for k, v in value_node.value 
                                if k.value not in existing_mapping
                            ]
                        )
                    else:
                        # Overwrite or add new key-value pair
                        existing_mapping[new_key] = new_value
                
                # Convert the merged mapping back to a list of tuples
                merged[key] = MappingNode(
                    tag=existing_value_node.tag,
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