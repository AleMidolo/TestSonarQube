def deep_merge_nodes(nodes):
    merged = {}
    
    # Iterate through nodes in reverse order so last value wins for non-mapping collisions
    for key_node, value_node in reversed(nodes):
        key = key_node.value
        
        if key not in merged:
            # First time seeing this key, just store the value
            merged[key] = (key_node, value_node)
            continue
            
        # We've seen this key before - need to merge
        existing_value_node = merged[key][1]
        
        # If both nodes are mappings, do a deep merge
        if (value_node.tag == 'tag:yaml.org,2002:map' and 
            existing_value_node.tag == 'tag:yaml.org,2002:map'):
            
            # Recursively merge the nested mapping nodes
            merged_value = deep_merge_nodes(value_node.value + existing_value_node.value)
            
            # Create new MappingNode with merged values
            merged[key] = (
                key_node,
                type(value_node)(
                    tag='tag:yaml.org,2002:map',
                    value=merged_value
                )
            )
        else:
            # For non-mapping nodes, keep the existing value since we're iterating in reverse
            merged[key] = merged[key]
            
    # Convert merged dict back to list of tuples
    return list(merged.values())